#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Any


MASSES = (
    60, 65, 70, 75, 80, 85, 90, 95,
    100, 105, 110, 115, 120, 125, 130, 135, 140,
    160, 180, 200, 250, 300, 350, 400, 450, 500,
    600, 700, 800, 900, 1000, 1100, 1200, 1400,
    1600, 1800, 2000, 2300, 2600, 2900, 3200, 3500,
)

CAMPAIGN = (
    "RunIII2024Summer24NanoAODv15-"
    "150X_mcRun3_2024_realistic_v2-v2"
)

DATA_TIER = "NANOAODSIM"


@dataclass(frozen=True)
class SampleFamily:
    section: str
    dataset_name: str
    process_expression: str
    primary_dataset: str
    id_base: int


FAMILIES = (
    SampleFamily(
        section="gluon-gluon fusion",
        dataset_name="ggphi_phitt_{mass}",
        process_expression=(
            'procs.ggphi_phitt.get_process("ggphi_phitt_{mass}")'
        ),
        primary_dataset=(
            "GluGluH-Hto2Tau_Par-M-{mass}-2HDM-II_"
            "TuneCP5_13p6TeV_powheg-pythia8"
        ),
        id_base=24_100_000,
    ),
    SampleFamily(
        section="b-associated production",
        dataset_name="bbphi_phitt_{mass}",
        process_expression=(
            'procs.bbphi_phitt.get_process("bbphi_phitt_{mass}")'
        ),
        primary_dataset=(
            "BBH-Hto2Tau_Par-M-{mass}_"
            "TuneCP5_13p6TeV_powheg-pythia8"
        ),
        id_base=24_200_000,
    ),
)


def run_das(query: str, *, json_output: bool = False) -> str:
    command = [
        "dasgoclient",
        f"--query={query}",
        "--limit=0",
    ]

    if json_output:
        command.append("--json")

    result = subprocess.run(
        command,
        check=True,
        capture_output=True,
        text=True,
    )

    return result.stdout.strip()


def build_dataset_name(family: SampleFamily, mass: int) -> str:
    primary = family.primary_dataset.format(mass=mass)

    return f"/{primary}/{CAMPAIGN}/{DATA_TIER}"


def dataset_exists(dataset: str) -> bool:
    output = run_das(f"dataset dataset={dataset}")

    return dataset in {
        line.strip()
        for line in output.splitlines()
        if line.strip()
    }


def get_summary(dataset: str) -> tuple[int, int]:
    output = run_das(
        f"summary dataset={dataset}",
        json_output=True,
    )

    payload: list[dict[str, Any]] = json.loads(output)

    summaries = [
        summary
        for record in payload
        for summary in record.get("summary", [])
    ]

    if len(summaries) != 1:
        raise RuntimeError(
            f"Expected exactly one summary for {dataset}, "
            f"found {len(summaries)}"
        )

    summary = summaries[0]

    return int(summary["nfiles"]), int(summary["nevents"])


def render_dataset(
    *,
    family: SampleFamily,
    mass: int,
    dataset: str,
    n_files: int,
    n_events: int,
) -> str:
    name = family.dataset_name.format(mass=mass)
    section = family.process_expression.format(mass=mass)
    dataset_id = family.id_base + mass

    return f'''cpn.add_dataset(
    name="{name}",
    id={dataset_id},
    processes=[{section}],
    keys=[
        "{dataset}",  # noqa
    ],
    n_files={n_files},
    n_events={n_events},
)'''


def render_file() -> str:
    blocks = [
        '''# coding: utf-8

"""
Signal datasets for the 2024 data-taking campaign with datasets at NanoAOD tier in version 15.
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2024_nano_v15 import campaign_run3_2024_nano_v15 as cpn
'''.rstrip()
    ]

    for family in FAMILIES:
        family_blocks = [
            f"""
#
# {family.section}
#
""".strip()
        ]

        for mass in MASSES:
            dataset = build_dataset_name(family, mass)

            if not dataset_exists(dataset):
                raise RuntimeError(
                    f"Dataset does not exist in DAS:\n{dataset}"
                )

            n_files, n_events = get_summary(dataset)

            family_blocks.append(
                render_dataset(
                    family=family,
                    mass=mass,
                    dataset=dataset,
                    n_files=n_files,
                    n_events=n_events,
                )
            )

            print(
                f"{family.section}: M={mass}: "
                f"{n_files} files, {n_events} events"
            )

        blocks.append("\n\n".join(family_blocks))

    return "\n\n\n".join(blocks) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        required=True,
    )
    args = parser.parse_args()

    content = render_file()
    args.output.write_text(content, encoding="utf-8")


if __name__ == "__main__":
    main()

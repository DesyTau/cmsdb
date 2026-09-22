# coding: utf-8

"""
Signal datasets for the 2024 data-taking campaign with datasets at NanoAOD tier in version 15.
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2024_nano_v15 import campaign_run3_2024_nano_v15 as cpn


#
# gluon-gluon fusion
#

cpn.add_dataset(
    name="ggphi_phitt_60",
    id=24100060,
    processes=[procs.ggphi_phitt.get_process("ggphi_phitt_60")],
    keys=[
        "/GluGluH-Hto2Tau_Par-M-60-2HDM-II_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=56,
    n_events=6200000,
)

cpn.add_dataset(
    name="ggphi_phitt_65",
    id=24100065,
    processes=[procs.ggphi_phitt.get_process("ggphi_phitt_65")],
    keys=[
        "/GluGluH-Hto2Tau_Par-M-65-2HDM-II_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=100,
    n_events=6200000,
)

cpn.add_dataset(
    name="ggphi_phitt_70",
    id=24100070,
    processes=[procs.ggphi_phitt.get_process("ggphi_phitt_70")],
    keys=[
        "/GluGluH-Hto2Tau_Par-M-70-2HDM-II_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=100,
    n_events=6187274,
)

cpn.add_dataset(
    name="ggphi_phitt_75",
    id=24100075,
    processes=[procs.ggphi_phitt.get_process("ggphi_phitt_75")],
    keys=[
        "/GluGluH-Hto2Tau_Par-M-75-2HDM-II_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=79,
    n_events=6200000,
)

cpn.add_dataset(
    name="ggphi_phitt_80",
    id=24100080,
    processes=[procs.ggphi_phitt.get_process("ggphi_phitt_80")],
    keys=[
        "/GluGluH-Hto2Tau_Par-M-80-2HDM-II_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=99,
    n_events=6199291,
)

cpn.add_dataset(
    name="ggphi_phitt_85",
    id=24100085,
    processes=[procs.ggphi_phitt.get_process("ggphi_phitt_85")],
    keys=[
        "/GluGluH-Hto2Tau_Par-M-85-2HDM-II_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=124,
    n_events=6145792,
)

cpn.add_dataset(
    name="ggphi_phitt_90",
    id=24100090,
    processes=[procs.ggphi_phitt.get_process("ggphi_phitt_90")],
    keys=[
        "/GluGluH-Hto2Tau_Par-M-90-2HDM-II_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=54,
    n_events=6200000,
)

cpn.add_dataset(
    name="ggphi_phitt_95",
    id=24100095,
    processes=[procs.ggphi_phitt.get_process("ggphi_phitt_95")],
    keys=[
        "/GluGluH-Hto2Tau_Par-M-95-2HDM-II_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=97,
    n_events=6200000,
)

cpn.add_dataset(
    name="ggphi_phitt_100",
    id=24100100,
    processes=[procs.ggphi_phitt.get_process("ggphi_phitt_100")],
    keys=[
        "/GluGluH-Hto2Tau_Par-M-100-2HDM-II_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=79,
    n_events=6200000,
)

cpn.add_dataset(
    name="ggphi_phitt_105",
    id=24100105,
    processes=[procs.ggphi_phitt.get_process("ggphi_phitt_105")],
    keys=[
        "/GluGluH-Hto2Tau_Par-M-105-2HDM-II_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=71,
    n_events=6200000,
)

cpn.add_dataset(
    name="ggphi_phitt_110",
    id=24100110,
    processes=[procs.ggphi_phitt.get_process("ggphi_phitt_110")],
    keys=[
        "/GluGluH-Hto2Tau_Par-M-110-2HDM-II_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=100,
    n_events=6183739,
)

cpn.add_dataset(
    name="ggphi_phitt_115",
    id=24100115,
    processes=[procs.ggphi_phitt.get_process("ggphi_phitt_115")],
    keys=[
        "/GluGluH-Hto2Tau_Par-M-115-2HDM-II_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=79,
    n_events=6199296,
)

cpn.add_dataset(
    name="ggphi_phitt_120",
    id=24100120,
    processes=[procs.ggphi_phitt.get_process("ggphi_phitt_120")],
    keys=[
        "/GluGluH-Hto2Tau_Par-M-120-2HDM-II_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=57,
    n_events=6200000,
)

cpn.add_dataset(
    name="ggphi_phitt_125",
    id=24100125,
    processes=[procs.ggphi_phitt.get_process("ggphi_phitt_125")],
    keys=[
        "/GluGluH-Hto2Tau_Par-M-125-2HDM-II_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=78,
    n_events=6200000,
)

cpn.add_dataset(
    name="ggphi_phitt_130",
    id=24100130,
    processes=[procs.ggphi_phitt.get_process("ggphi_phitt_130")],
    keys=[
        "/GluGluH-Hto2Tau_Par-M-130-2HDM-II_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=73,
    n_events=6199296,
)

cpn.add_dataset(
    name="ggphi_phitt_135",
    id=24100135,
    processes=[procs.ggphi_phitt.get_process("ggphi_phitt_135")],
    keys=[
        "/GluGluH-Hto2Tau_Par-M-135-2HDM-II_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=55,
    n_events=6200000,
)

cpn.add_dataset(
    name="ggphi_phitt_140",
    id=24100140,
    processes=[procs.ggphi_phitt.get_process("ggphi_phitt_140")],
    keys=[
        "/GluGluH-Hto2Tau_Par-M-140-2HDM-II_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=85,
    n_events=6190116,
)

cpn.add_dataset(
    name="ggphi_phitt_160",
    id=24100160,
    processes=[procs.ggphi_phitt.get_process("ggphi_phitt_160")],
    keys=[
        "/GluGluH-Hto2Tau_Par-M-160-2HDM-II_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=77,
    n_events=6188720,
)

cpn.add_dataset(
    name="ggphi_phitt_180",
    id=24100180,
    processes=[procs.ggphi_phitt.get_process("ggphi_phitt_180")],
    keys=[
        "/GluGluH-Hto2Tau_Par-M-180-2HDM-II_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=86,
    n_events=6200000,
)

cpn.add_dataset(
    name="ggphi_phitt_200",
    id=24100200,
    processes=[procs.ggphi_phitt.get_process("ggphi_phitt_200")],
    keys=[
        "/GluGluH-Hto2Tau_Par-M-200-2HDM-II_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=88,
    n_events=6200000,
)

cpn.add_dataset(
    name="ggphi_phitt_250",
    id=24100250,
    processes=[procs.ggphi_phitt.get_process("ggphi_phitt_250")],
    keys=[
        "/GluGluH-Hto2Tau_Par-M-250-2HDM-II_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=49,
    n_events=6200000,
)

cpn.add_dataset(
    name="ggphi_phitt_300",
    id=24100300,
    processes=[procs.ggphi_phitt.get_process("ggphi_phitt_300")],
    keys=[
        "/GluGluH-Hto2Tau_Par-M-300-2HDM-II_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=54,
    n_events=6198596,
)

cpn.add_dataset(
    name="ggphi_phitt_350",
    id=24100350,
    processes=[procs.ggphi_phitt.get_process("ggphi_phitt_350")],
    keys=[
        "/GluGluH-Hto2Tau_Par-M-350-2HDM-II_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=106,
    n_events=6198586,
)

cpn.add_dataset(
    name="ggphi_phitt_400",
    id=24100400,
    processes=[procs.ggphi_phitt.get_process("ggphi_phitt_400")],
    keys=[
        "/GluGluH-Hto2Tau_Par-M-400-2HDM-II_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=50,
    n_events=6199289,
)

cpn.add_dataset(
    name="ggphi_phitt_450",
    id=24100450,
    processes=[procs.ggphi_phitt.get_process("ggphi_phitt_450")],
    keys=[
        "/GluGluH-Hto2Tau_Par-M-450-2HDM-II_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=162,
    n_events=6195065,
)

cpn.add_dataset(
    name="ggphi_phitt_500",
    id=24100500,
    processes=[procs.ggphi_phitt.get_process("ggphi_phitt_500")],
    keys=[
        "/GluGluH-Hto2Tau_Par-M-500-2HDM-II_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=51,
    n_events=6200000,
)

cpn.add_dataset(
    name="ggphi_phitt_600",
    id=24100600,
    processes=[procs.ggphi_phitt.get_process("ggphi_phitt_600")],
    keys=[
        "/GluGluH-Hto2Tau_Par-M-600-2HDM-II_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=75,
    n_events=6196460,
)

cpn.add_dataset(
    name="ggphi_phitt_700",
    id=24100700,
    processes=[procs.ggphi_phitt.get_process("ggphi_phitt_700")],
    keys=[
        "/GluGluH-Hto2Tau_Par-M-700-2HDM-II_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=141,
    n_events=6192990,
)

cpn.add_dataset(
    name="ggphi_phitt_800",
    id=24100800,
    processes=[procs.ggphi_phitt.get_process("ggphi_phitt_800")],
    keys=[
        "/GluGluH-Hto2Tau_Par-M-800-2HDM-II_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=58,
    n_events=6200000,
)

cpn.add_dataset(
    name="ggphi_phitt_900",
    id=24100900,
    processes=[procs.ggphi_phitt.get_process("ggphi_phitt_900")],
    keys=[
        "/GluGluH-Hto2Tau_Par-M-900-2HDM-II_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=127,
    n_events=6197909,
)

cpn.add_dataset(
    name="ggphi_phitt_1000",
    id=24101000,
    processes=[procs.ggphi_phitt.get_process("ggphi_phitt_1000")],
    keys=[
        "/GluGluH-Hto2Tau_Par-M-1000-2HDM-II_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=67,
    n_events=6200000,
)

cpn.add_dataset(
    name="ggphi_phitt_1100",
    id=24101100,
    processes=[procs.ggphi_phitt.get_process("ggphi_phitt_1100")],
    keys=[
        "/GluGluH-Hto2Tau_Par-M-1100-2HDM-II_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=102,
    n_events=6199304,
)

cpn.add_dataset(
    name="ggphi_phitt_1200",
    id=24101200,
    processes=[procs.ggphi_phitt.get_process("ggphi_phitt_1200")],
    keys=[
        "/GluGluH-Hto2Tau_Par-M-1200-2HDM-II_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=66,
    n_events=6200000,
)

cpn.add_dataset(
    name="ggphi_phitt_1400",
    id=24101400,
    processes=[procs.ggphi_phitt.get_process("ggphi_phitt_1400")],
    keys=[
        "/GluGluH-Hto2Tau_Par-M-1400-2HDM-II_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=83,
    n_events=6200000,
)

cpn.add_dataset(
    name="ggphi_phitt_1600",
    id=24101600,
    processes=[procs.ggphi_phitt.get_process("ggphi_phitt_1600")],
    keys=[
        "/GluGluH-Hto2Tau_Par-M-1600-2HDM-II_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=66,
    n_events=6199310,
)

cpn.add_dataset(
    name="ggphi_phitt_1800",
    id=24101800,
    processes=[procs.ggphi_phitt.get_process("ggphi_phitt_1800")],
    keys=[
        "/GluGluH-Hto2Tau_Par-M-1800-2HDM-II_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=136,
    n_events=6200000,
)

cpn.add_dataset(
    name="ggphi_phitt_2000",
    id=24102000,
    processes=[procs.ggphi_phitt.get_process("ggphi_phitt_2000")],
    keys=[
        "/GluGluH-Hto2Tau_Par-M-2000-2HDM-II_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=92,
    n_events=6200000,
)

cpn.add_dataset(
    name="ggphi_phitt_2300",
    id=24102300,
    processes=[procs.ggphi_phitt.get_process("ggphi_phitt_2300")],
    keys=[
        "/GluGluH-Hto2Tau_Par-M-2300-2HDM-II_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=125,
    n_events=6197936,
)

cpn.add_dataset(
    name="ggphi_phitt_2600",
    id=24102600,
    processes=[procs.ggphi_phitt.get_process("ggphi_phitt_2600")],
    keys=[
        "/GluGluH-Hto2Tau_Par-M-2600-2HDM-II_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=96,
    n_events=6200000,
)

cpn.add_dataset(
    name="ggphi_phitt_2900",
    id=24102900,
    processes=[procs.ggphi_phitt.get_process("ggphi_phitt_2900")],
    keys=[
        "/GluGluH-Hto2Tau_Par-M-2900-2HDM-II_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=84,
    n_events=6200000,
)

cpn.add_dataset(
    name="ggphi_phitt_3200",
    id=24103200,
    processes=[procs.ggphi_phitt.get_process("ggphi_phitt_3200")],
    keys=[
        "/GluGluH-Hto2Tau_Par-M-3200-2HDM-II_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=63,
    n_events=6200000,
)

cpn.add_dataset(
    name="ggphi_phitt_3500",
    id=24103500,
    processes=[procs.ggphi_phitt.get_process("ggphi_phitt_3500")],
    keys=[
        "/GluGluH-Hto2Tau_Par-M-3500-2HDM-II_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=107,
    n_events=6199317,
)


#
# b-associated production
#

cpn.add_dataset(
    name="bbphi_phitt_60",
    id=24200060,
    processes=[procs.bbphi_phitt.get_process("bbphi_phitt_60")],
    keys=[
        "/BBH-Hto2Tau_Par-M-60_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=87,
    n_events=1791300,
)

cpn.add_dataset(
    name="bbphi_phitt_65",
    id=24200065,
    processes=[procs.bbphi_phitt.get_process("bbphi_phitt_65")],
    keys=[
        "/BBH-Hto2Tau_Par-M-65_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=45,
    n_events=1800000,
)

cpn.add_dataset(
    name="bbphi_phitt_70",
    id=24200070,
    processes=[procs.bbphi_phitt.get_process("bbphi_phitt_70")],
    keys=[
        "/BBH-Hto2Tau_Par-M-70_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=19,
    n_events=1800000,
)

cpn.add_dataset(
    name="bbphi_phitt_75",
    id=24200075,
    processes=[procs.bbphi_phitt.get_process("bbphi_phitt_75")],
    keys=[
        "/BBH-Hto2Tau_Par-M-75_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=58,
    n_events=1800000,
)

cpn.add_dataset(
    name="bbphi_phitt_80",
    id=24200080,
    processes=[procs.bbphi_phitt.get_process("bbphi_phitt_80")],
    keys=[
        "/BBH-Hto2Tau_Par-M-80_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=65,
    n_events=1799305,
)

cpn.add_dataset(
    name="bbphi_phitt_85",
    id=24200085,
    processes=[procs.bbphi_phitt.get_process("bbphi_phitt_85")],
    keys=[
        "/BBH-Hto2Tau_Par-M-85_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=38,
    n_events=1800000,
)

cpn.add_dataset(
    name="bbphi_phitt_90",
    id=24200090,
    processes=[procs.bbphi_phitt.get_process("bbphi_phitt_90")],
    keys=[
        "/BBH-Hto2Tau_Par-M-90_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=61,
    n_events=1800000,
)

cpn.add_dataset(
    name="bbphi_phitt_95",
    id=24200095,
    processes=[procs.bbphi_phitt.get_process("bbphi_phitt_95")],
    keys=[
        "/BBH-Hto2Tau_Par-M-95_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=28,
    n_events=1799308,
)

cpn.add_dataset(
    name="bbphi_phitt_100",
    id=24200100,
    processes=[procs.bbphi_phitt.get_process("bbphi_phitt_100")],
    keys=[
        "/BBH-Hto2Tau_Par-M-100_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=59,
    n_events=1800000,
)

cpn.add_dataset(
    name="bbphi_phitt_105",
    id=24200105,
    processes=[procs.bbphi_phitt.get_process("bbphi_phitt_105")],
    keys=[
        "/BBH-Hto2Tau_Par-M-105_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=58,
    n_events=1798614,
)

cpn.add_dataset(
    name="bbphi_phitt_110",
    id=24200110,
    processes=[procs.bbphi_phitt.get_process("bbphi_phitt_110")],
    keys=[
        "/BBH-Hto2Tau_Par-M-110_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=38,
    n_events=1774084,
)

cpn.add_dataset(
    name="bbphi_phitt_115",
    id=24200115,
    processes=[procs.bbphi_phitt.get_process("bbphi_phitt_115")],
    keys=[
        "/BBH-Hto2Tau_Par-M-115_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=34,
    n_events=1800000,
)

cpn.add_dataset(
    name="bbphi_phitt_120",
    id=24200120,
    processes=[procs.bbphi_phitt.get_process("bbphi_phitt_120")],
    keys=[
        "/BBH-Hto2Tau_Par-M-120_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=21,
    n_events=1798620,
)

cpn.add_dataset(
    name="bbphi_phitt_125",
    id=24200125,
    processes=[procs.bbphi_phitt.get_process("bbphi_phitt_125")],
    keys=[
        "/BBH-Hto2Tau_Par-M-125_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=31,
    n_events=1754262,
)

cpn.add_dataset(
    name="bbphi_phitt_130",
    id=24200130,
    processes=[procs.bbphi_phitt.get_process("bbphi_phitt_130")],
    keys=[
        "/BBH-Hto2Tau_Par-M-130_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=33,
    n_events=1783464,
)

cpn.add_dataset(
    name="bbphi_phitt_135",
    id=24200135,
    processes=[procs.bbphi_phitt.get_process("bbphi_phitt_135")],
    keys=[
        "/BBH-Hto2Tau_Par-M-135_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=71,
    n_events=1793380,
)

cpn.add_dataset(
    name="bbphi_phitt_140",
    id=24200140,
    processes=[procs.bbphi_phitt.get_process("bbphi_phitt_140")],
    keys=[
        "/BBH-Hto2Tau_Par-M-140_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=57,
    n_events=1800000,
)

cpn.add_dataset(
    name="bbphi_phitt_160",
    id=24200160,
    processes=[procs.bbphi_phitt.get_process("bbphi_phitt_160")],
    keys=[
        "/BBH-Hto2Tau_Par-M-160_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=23,
    n_events=1800000,
)

cpn.add_dataset(
    name="bbphi_phitt_180",
    id=24200180,
    processes=[procs.bbphi_phitt.get_process("bbphi_phitt_180")],
    keys=[
        "/BBH-Hto2Tau_Par-M-180_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=55,
    n_events=1800000,
)

cpn.add_dataset(
    name="bbphi_phitt_200",
    id=24200200,
    processes=[procs.bbphi_phitt.get_process("bbphi_phitt_200")],
    keys=[
        "/BBH-Hto2Tau_Par-M-200_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=40,
    n_events=1800000,
)

cpn.add_dataset(
    name="bbphi_phitt_250",
    id=24200250,
    processes=[procs.bbphi_phitt.get_process("bbphi_phitt_250")],
    keys=[
        "/BBH-Hto2Tau_Par-M-250_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=52,
    n_events=878636,
)

cpn.add_dataset(
    name="bbphi_phitt_300",
    id=24200300,
    processes=[procs.bbphi_phitt.get_process("bbphi_phitt_300")],
    keys=[
        "/BBH-Hto2Tau_Par-M-300_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=24,
    n_events=880000,
)

cpn.add_dataset(
    name="bbphi_phitt_350",
    id=24200350,
    processes=[procs.bbphi_phitt.get_process("bbphi_phitt_350")],
    keys=[
        "/BBH-Hto2Tau_Par-M-350_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=23,
    n_events=880000,
)

cpn.add_dataset(
    name="bbphi_phitt_400",
    id=24200400,
    processes=[procs.bbphi_phitt.get_process("bbphi_phitt_400")],
    keys=[
        "/BBH-Hto2Tau_Par-M-400_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=880000,
)

cpn.add_dataset(
    name="bbphi_phitt_450",
    id=24200450,
    processes=[procs.bbphi_phitt.get_process("bbphi_phitt_450")],
    keys=[
        "/BBH-Hto2Tau_Par-M-450_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=53,
    n_events=878672,
)

cpn.add_dataset(
    name="bbphi_phitt_500",
    id=24200500,
    processes=[procs.bbphi_phitt.get_process("bbphi_phitt_500")],
    keys=[
        "/BBH-Hto2Tau_Par-M-500_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=28,
    n_events=880000,
)

cpn.add_dataset(
    name="bbphi_phitt_600",
    id=24200600,
    processes=[procs.bbphi_phitt.get_process("bbphi_phitt_600")],
    keys=[
        "/BBH-Hto2Tau_Par-M-600_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=440000,
)

cpn.add_dataset(
    name="bbphi_phitt_700",
    id=24200700,
    processes=[procs.bbphi_phitt.get_process("bbphi_phitt_700")],
    keys=[
        "/BBH-Hto2Tau_Par-M-700_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=440000,
)

cpn.add_dataset(
    name="bbphi_phitt_800",
    id=24200800,
    processes=[procs.bbphi_phitt.get_process("bbphi_phitt_800")],
    keys=[
        "/BBH-Hto2Tau_Par-M-800_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=32,
    n_events=440000,
)

cpn.add_dataset(
    name="bbphi_phitt_900",
    id=24200900,
    processes=[procs.bbphi_phitt.get_process("bbphi_phitt_900")],
    keys=[
        "/BBH-Hto2Tau_Par-M-900_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=29,
    n_events=439338,
)

cpn.add_dataset(
    name="bbphi_phitt_1000",
    id=24201000,
    processes=[procs.bbphi_phitt.get_process("bbphi_phitt_1000")],
    keys=[
        "/BBH-Hto2Tau_Par-M-1000_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=29,
    n_events=440000,
)

cpn.add_dataset(
    name="bbphi_phitt_1100",
    id=24201100,
    processes=[procs.bbphi_phitt.get_process("bbphi_phitt_1100")],
    keys=[
        "/BBH-Hto2Tau_Par-M-1100_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=27,
    n_events=440000,
)

cpn.add_dataset(
    name="bbphi_phitt_1200",
    id=24201200,
    processes=[procs.bbphi_phitt.get_process("bbphi_phitt_1200")],
    keys=[
        "/BBH-Hto2Tau_Par-M-1200_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=240000,
)

cpn.add_dataset(
    name="bbphi_phitt_1400",
    id=24201400,
    processes=[procs.bbphi_phitt.get_process("bbphi_phitt_1400")],
    keys=[
        "/BBH-Hto2Tau_Par-M-1400_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=25,
    n_events=240000,
)

cpn.add_dataset(
    name="bbphi_phitt_1600",
    id=24201600,
    processes=[procs.bbphi_phitt.get_process("bbphi_phitt_1600")],
    keys=[
        "/BBH-Hto2Tau_Par-M-1600_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=240000,
)

cpn.add_dataset(
    name="bbphi_phitt_1800",
    id=24201800,
    processes=[procs.bbphi_phitt.get_process("bbphi_phitt_1800")],
    keys=[
        "/BBH-Hto2Tau_Par-M-1800_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=27,
    n_events=239346,
)

cpn.add_dataset(
    name="bbphi_phitt_2000",
    id=24202000,
    processes=[procs.bbphi_phitt.get_process("bbphi_phitt_2000")],
    keys=[
        "/BBH-Hto2Tau_Par-M-2000_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=26,
    n_events=240000,
)

cpn.add_dataset(
    name="bbphi_phitt_2300",
    id=24202300,
    processes=[procs.bbphi_phitt.get_process("bbphi_phitt_2300")],
    keys=[
        "/BBH-Hto2Tau_Par-M-2300_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=33,
    n_events=240000,
)

cpn.add_dataset(
    name="bbphi_phitt_2600",
    id=24202600,
    processes=[procs.bbphi_phitt.get_process("bbphi_phitt_2600")],
    keys=[
        "/BBH-Hto2Tau_Par-M-2600_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=26,
    n_events=240000,
)

cpn.add_dataset(
    name="bbphi_phitt_2900",
    id=24202900,
    processes=[procs.bbphi_phitt.get_process("bbphi_phitt_2900")],
    keys=[
        "/BBH-Hto2Tau_Par-M-2900_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=28,
    n_events=240000,
)

cpn.add_dataset(
    name="bbphi_phitt_3200",
    id=24203200,
    processes=[procs.bbphi_phitt.get_process("bbphi_phitt_3200")],
    keys=[
        "/BBH-Hto2Tau_Par-M-3200_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=27,
    n_events=240000,
)

cpn.add_dataset(
    name="bbphi_phitt_3500",
    id=24203500,
    processes=[procs.bbphi_phitt.get_process("bbphi_phitt_3500")],
    keys=[
        "/BBH-Hto2Tau_Par-M-3500_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=27,
    n_events=238794,
)

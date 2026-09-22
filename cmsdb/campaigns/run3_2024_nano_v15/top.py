# coding: utf-8

"""
Top quark related datasets for the 2024 data-taking campaign with datasets at NanoAOD tier in version 15.
"""

from order import DatasetInfo

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2024_nano_v15 import campaign_run3_2024_nano_v15 as cpn


#
# ttbar
#

cpn.add_dataset(
    name="TTto2L2Nu",
    id=470123263,
    processes=[procs.tt_dl],
    keys=[
        "/TTto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v3/NANOAODSIM",  # noqa
    ],
    n_files=780,
    n_events=470123263,
)

cpn.add_dataset(
    name="TTtoLNu2Q",
    id=484475057,
    processes=[procs.tt_sl],
    keys=[
        "/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=790,
    n_events=484475057,
)

cpn.add_dataset(
    name="TTto4Q",
    id=472535695,
    processes=[procs.tt_fh],
    keys=[
        "/TTto4Q_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=773,
    n_events=472535695,
)

#
# single top
#

cpn.add_dataset(
    name="TWminusto4Q",
    id=23999000,
    processes=[procs.st_twchannel_t_fh],
    keys=[
        "/TWminusto4Q_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=154,
    n_events=23999000,
)

cpn.add_dataset(
    name="TbarWplusto4Q",
    id=24000000,
    processes=[procs.st_twchannel_tbar_fh],
    keys=[
        "/TbarWplusto4Q_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=195,
    n_events=24000000,
)

cpn.add_dataset(
    name="TWminusto2L2Nu",
    id=14998000,
    processes=[procs.st_twchannel_t_dl],
    keys=[
        "/TWminusto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=176,
    n_events=14998000,
)

cpn.add_dataset(
    name="TbarWplusto2L2Nu",
    id=15000000,
    processes=[procs.st_twchannel_tbar_dl],
    keys=[
        "/TbarWplusto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=90,
    n_events=15000000,
)

cpn.add_dataset(
    name="TWminustoLNu2Q",
    id=28763293,
    processes=[procs.st_twchannel_t_sl],
    keys=[
        "/TWminustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],  
    n_files=252,
    n_events=28763293,
)

cpn.add_dataset(
    name="TbarWplustoLNu2Q",
    id=29395659,
    processes=[procs.st_twchannel_tbar_sl],
    keys=[
        "/TbarWplustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=252,
    n_events=29395659,
)


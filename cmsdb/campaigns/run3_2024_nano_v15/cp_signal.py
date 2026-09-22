# coding: utf-8

"""
Signal datasets for the 2024 data-taking campaign with datasets at NanoAOD tier in version 15.
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2024_nano_v15 import campaign_run3_2024_nano_v15 as cpn
from order import DatasetInfo


#
# Gluon-gluon fusion
#

cpn.add_dataset(
    name="h_ggf_htt_sm_prod_sm_filtered",
    id=96065865,
    processes=[procs.h_ggf_htt_sm_prod_sm],
    keys=[
        "/GluGluHJJto2TauUncorrelatedDecay-CP-even_Fil-Tau_Par-M-125_TuneCP5_13p6TeV_powhegMINLO-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=833,
    n_events=96065865,
)

cpn.add_dataset(
    name="h_ggf_htt_sm_prod_cpo_filtered",
    id=91419994,
    processes=[procs.h_ggf_htt_sm_prod_cpo],
    keys=[
        "/GluGluHJJto2TauUncorrelatedDecay-CP-odd_Fil-Tau_Par-M-125_TuneCP5_13p6TeV_powhegMINLO-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=782,
    n_events=91419994,
)

cpn.add_dataset(
    name="h_ggf_htt_sm_prod_mm_filtered",
    id=81239002,
    processes=[procs.h_ggf_htt_sm_prod_mm],
    keys=[
        "/GluGluHJJto2TauUncorrelatedDecay-CP-mix_Fil-Tau_Par-M-125_TuneCP5_13p6TeV_powhegMINLO-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=637,
    n_events=81239002,
)

cpn.add_dataset(
    name="h_vbf_htt_sm_filtered",
    id=54762069,
    processes=[procs.h_vbf_htt_sm],
    keys=[
        "/VBFH-Hto2TauUncorrelatedDecay_Fil-TauFilter_Par-M-125_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=398,
    n_events=54762069,
)


cpn.add_dataset(
    name="zh_htt_sm_filtered",
    id=8001416,
    processes=[procs.zh_htt_sm],
    keys=[
        "/ZH-Hto2TauUncorrelatedDecay_Fil-TauFilter_Par-M-125_TuneCP5_13p6TeV_powhegMINNLO-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v6/NANOAODSIM",  # noqa
    ],
    n_files=273,
    n_events=8001416,
)

cpn.add_dataset(
    name="wph_htt_sm_filtered",
    id=9006688,
    processes=[procs.wph_htt_sm],
    keys=[
        "/WplusH-Hto2TauUncorrelatedDecay_Fil-TauFilter_Par-M-125_TuneCP5_13p6TeV_powhegMINNLO-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=97,
    n_events=9006688,
)

cpn.add_dataset(
    name="wmh_htt_sm_filtered",
    id=6498588,
    processes=[procs.wmh_htt_sm],
    keys=[
        "/WminusH-Hto2TauUncorrelatedDecay_Fil-TauFilter_Par-M-125_TuneCP5_13p6TeV_powhegMINNLO-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=110,
    n_events=6498588,
)
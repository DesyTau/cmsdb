# coding: utf-8

"""
Electroweak datasets for the 2024 data-taking campaign with datasets at NanoAOD tier in version 15.
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2024_nano_v15 import campaign_run3_2024_nano_v15 as cpn
from order import DatasetInfo

#
# Drell-Yan to 2E, amcatnlo
#

cpn.add_dataset(
    name="DYto2E_MLL_10to50_amcatnloFXFX",
    id=139117188,
    processes=[procs.dy_ee_m10to50],
    keys=[
        "/DYto2E-2Jets_Bin-MLL-10to50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=694,
    n_events=139117188,
)

cpn.add_dataset(
    name="DYto2E_MLL_50_0J_amcatnloFXFX",
    id=4453230267,
    processes=[procs.dy_ee_m50_0j],
    keys=[
        "/DYto2E-2Jets_Bin-0J-MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=548,
    n_events=4453230267,
)

cpn.add_dataset(
    name="DYto2E_MLL_50_1J_amcatnloFXFX",
    id=338867940,
    processes=[procs.dy_ee_m50_1j],
    keys=[
        "/DYto2E-2Jets_Bin-1J-MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v3/NANOAODSIM",  # noqa
    ],
    n_files=2108,
    n_events=338867940,
)

cpn.add_dataset(
    name="DYto2E_MLL_50_2J_amcatnloFXFX",
    id=307042054,
    processes=[procs.dy_ee_m50_2j],
    keys=[
        "/DYto2E-2Jets_Bin-2J-MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=317,
    n_events=307042054,
)

cpn.add_dataset(
    name="DYto2E_MLL_50_amcatnloFXFX",
    id=486448139,
    processes=[procs.dy_ee_m50],
    keys=[
        "/DYto2E-2Jets_Bin-MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v4/NANOAODSIM",  # noqa
    ],
    n_files=2990,
    n_events=486448139,
)

#
# Drell-Yan to 2Mu, amcatnlo
#

cpn.add_dataset(
    name="DYto2Mu_MLL_10to50_amcatnloFXFX",
    id=144889491,
    processes=[procs.dy_mumu_m10to50],
    keys=[
        "/DYto2Mu-2Jets_Bin-MLL-10to50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=1015,
    n_events=144889491,
)

cpn.add_dataset(
    name="DYto2Mu_MLL_50_0J_amcatnloFXFX",
    id=466773211,
    processes=[procs.dy_mumu_m50_0j],
    keys=[
        "/DYto2Mu-2Jets_Bin-0J-MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v3/NANOAODSIM",  # noqa
    ],
    n_files=534,
    n_events=466773211,
)

cpn.add_dataset(
    name="DYto2Mu_MLL_50_1J_amcatnloFXFX",
    id=404580799,
    processes=[procs.dy_mumu_m50_1j],
    keys=[
        "/DYto2Mu-2Jets_Bin-1J-MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v1/NANOAODSIM",  # noqa
    ],
    n_files=327,
    n_events=404580799,
)

cpn.add_dataset(
    name="DYto2Mu_MLL_50_2J_amcatnloFXFX",
    id=285910646,
    processes=[procs.dy_mumu_m50_2j],
    keys=[
        "/DYto2Mu-2Jets_Bin-2J-MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v3/NANOAODSIM",  # noqa
    ],
    n_files=1739,
    n_events=285910646,
)

cpn.add_dataset(
    name="DYto2Mu_MLL_50_amcatnloFXFX",
    id=490076405,
    processes=[procs.dy_mumu_m50],
    keys=[
        "/DYto2Mu-2Jets_Bin-MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v6/NANOAODSIM",  # noqa
    ],
    n_files=1015,
    n_events=490076405,
)

#
# Drell-Yan to 2Tau, amcatnlo
#

# missing filtered samples

# cpn.add_dataset(
#     name="dy_tautau_m50toinf_amcatnlo",
#     id=349164447,
#     processes=[procs.dy_tt_m50],
#     keys=[
#         "/DYto2Tau-2Jets_Bin-MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v7/NANOAODSIM",  # noqa
#     ],
#     n_files=1837,
#     n_events=349164447,
# )

cpn.add_dataset(
    name="DYto2Tau_MLL_50_0J_amcatnloFXFX",
    id=493132017,
    processes=[procs.dy_tt_m50_0j],
    keys=[
        "/DYto2Tau-2Jets_Bin-0J-MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v4/NANOAODSIM",  # noqa
    ],
    n_files=2666,
    n_events=493132017,
)

cpn.add_dataset(
    name="DYto2Tau_MLL_50_1J_amcatnloFXFX",
    id=428387857,
    processes=[procs.dy_tt_m50_1j],
    keys=[
        "/DYto2Tau-2Jets_Bin-1J-MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=2026,
    n_events=428387857,
)

cpn.add_dataset(
    name="DYto2Tau_MLL_50_2J_amcatnloFXFX",
    id=232971613,
    processes=[procs.dy_tt_m50_2j],
    keys=[
        "/DYto2Tau-2Jets_Bin-2J-MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=1592,
    n_events=232971613,
)


#
# Diboson
#

cpn.add_dataset(
    name="WW",
    id=63986968,
    processes=[procs.ww],
    keys=[
        "/WW_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",
    ],
    n_files=518,
    n_events=63986968,
)

cpn.add_dataset(
    name="WZ",
    id=30547825,
    processes=[procs.wz],
    keys=[
        "/WZ_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",
    ],
    n_files=307,
    n_events=30547825,
)

cpn.add_dataset(
    name="ZZ",
    id=4800000,
    processes=[procs.zz],
    keys=[
        "/ZZ_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",
    ],
    n_files=76,
    n_events=4800000,
)

#
# Triboson
#

cpn.add_dataset(
    name="WWW_4F",
    id=4299284,
    processes=[procs.www],
    keys=[
        "/WWW-4F_TuneCP5_13p6TeV_amcatnlo-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",
    ],
    n_files=49,
    n_events=4299284,
)

cpn.add_dataset(
    name="WWZ_4F",
    id=16184379,
    processes=[procs.wwz],
    keys=[
        "/WWZ-4F_TuneCP5_13p6TeV_amcatnlo-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",
    ],
    n_files=171,
    n_events=16184379,
)

cpn.add_dataset(
    name="WZZ",
    id=16199286,
    processes=[procs.wzz],
    keys=[
        "/WZZ-5F_TuneCP5_13p6TeV_amcatnlo-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",
    ],
    n_files=127,
    n_events=16199286,
)

cpn.add_dataset(
    name="ZZZ",
    id=16192091,
    processes=[procs.zzz],
    keys=[
        "/ZZZ-5F_TuneCP5_13p6TeV_amcatnlo-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",
    ],
    n_files=201,
    n_events=16192091,
)

#
# W+jets
#

## missing inclusive sample

cpn.add_dataset(
    name="WtoLNu_1J_madgraphMLM",
    id=429800607,
    processes=[procs.wj_1j],
    keys=[
        "/WtoLNu-4Jets_Bin-1J_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
    ],
    n_files=2491,
    n_events=429800607,
)

cpn.add_dataset(
    name="WtoLNu_2J_madgraphMLM",
    id=286526689,
    processes=[procs.wj_2j],
    keys=[
        "/WtoLNu-4Jets_Bin-2J_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
    ],
    n_files=1632,
    n_events=286526689,
)

cpn.add_dataset(
    name="WtoLNu_3J_madgraphMLM",
    id=139773986,
    processes=[procs.wj_3j],
    keys=[
        "/WtoLNu-4Jets_Bin-3J_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
    ],
    n_files=915,
    n_events=139773986,
)

cpn.add_dataset(
    name="WtoLNu_4J_madgraphMLM",
    id=85950957,
    processes=[procs.wj_4j],
    keys=[
        "/WtoLNu-4Jets_Bin-4J_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
    ],
    n_files=644,
    n_events=85950957,
)
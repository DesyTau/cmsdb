# coding: utf-8

"""
Electroweak datasets for the 2024 data-taking campaign with datasets at NanoAOD tier in version 15.
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2024_nano_v15 import campaign_run3_2024_nano_v15 as cpn
from order import DatasetInfo

#
# Drell-Yan to 2L, amcatnlo
#

# missing inclusive and 0J samples. using pt-binned samples for 1J and 2J

# """ cpn.add_dataset(
#     name="dy_m50toinf_1j_pt40to100_amcatnlo",
#     id=15300236,
#     processes=[procs.dy_m50toinf_1j_pt40to100],
#     keys=[
#         "/DYto2L-2Jets_Bin-1J-MLL-50-PTLL-40to100_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v3/NANOAODSIM",  # noqa
#     ],
#     n_files=3045,
#     n_events=479655476,
# )

# cpn.add_dataset(
#     name="dy_m50toinf_1j_pt100to200_amcatnlo",
#     id=15304428,
#     processes=[procs.dy_m50toinf_1j_pt100to200],
#     keys=[
#         "/DYto2L-2Jets_Bin-1J-MLL-50-PTLL-100to200_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=355,
#     n_events=227319605,
# )

# cpn.add_dataset(
#     name="dy_m50toinf_1j_pt200to400_amcatnlo",
#     id=15304451,
#     processes=[procs.dy_m50toinf_1j_pt200to400],
#     keys=[
#         "/DYto2L-2Jets_Bin-1J-MLL-50-PTLL-200to400_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=54,
#     n_events=22383959,
# )

# cpn.add_dataset(
#     name="dy_m50toinf_1j_pt400to600_amcatnlo",
#     id=15304493,
#     processes=[procs.dy_m50toinf_1j_pt400to600],
#     keys=[
#         "/DYto2L-2Jets_Bin-1J-MLL-50-PTLL-400to600_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=58,
#     n_events=10404540,
# )

# cpn.add_dataset(
#     name="dy_m50toinf_1j_pt600toinf_amcatnlo",
#     id=15304449,
#     processes=[procs.dy_m50toinf_1j_pt600toinf],
#     keys=[
#         "/DYto2L-2Jets_Bin-1J-MLL-50-PTLL-600_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=42,
#     n_events=9996457,
# )

# cpn.add_dataset(
#     name="dy_m50toinf_2j_pt40to100_amcatnlo",
#     id=15300484,
#     processes=[procs.dy_m50toinf_2j_pt40to100],
#     keys=[
#         "/DYto2L-2Jets_Bin-2J-MLL-50-PTLL-40to100_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v3/NANOAODSIM",  # noqa
#     ],
#     n_files=1_787,
#     n_events=247167836,
# )

# cpn.add_dataset(
#     name="dy_m50toinf_2j_pt100to200_amcatnlo",
#     id=15296152,
#     processes=[procs.dy_m50toinf_2j_pt100to200],
#     keys=[
#         "/DYto2L-2Jets_Bin-2J-MLL-50-PTLL-100to200_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=389,
#     n_events=246696940,
# )

# cpn.add_dataset(
#     name="dy_m50toinf_2j_pt200to400_amcatnlo",
#     id=15304466,
#     processes=[procs.dy_m50toinf_2j_pt200to400],
#     keys=[
#         "/DYto2L-2Jets_Bin-2J-MLL-50-PTLL-200to400_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=139,
#     n_events=44028174,
# )

# cpn.add_dataset(
#     name="dy_m50toinf_2j_pt400to600_amcatnlo",
#     id=15304446,
#     processes=[procs.dy_m50toinf_2j_pt400to600],
#     keys=[
#         "/DYto2L-2Jets_Bin-2J-MLL-50-PTLL-400to600_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=47,
#     n_events=9893470,
# )

# cpn.add_dataset(
#     name="dy_m50toinf_2j_pt600toinf_amcatnlo",
#     id=15304548,
#     processes=[procs.dy_m50toinf_2j_pt600toinf],
#     keys=[
#         "/DYto2L-2Jets_Bin-2J-MLL-50-PTLL-600_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=50,
#     n_events=9801431,
# ) """

#
# Drell-Yan to 2E, amcatnlo
#

# cpn.add_dataset(
#     name="dy_ee_m50toinf_amcatnlo",
#     id=486448139,
#     processes=[procs.dy_ee_m50],
#     keys=[
#         "/DYto2E-2Jets_Bin-MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v4/NANOAODSIM",  # noqa
#     ],
#     n_files=2990,
#     n_events=486448139,
# )

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

#
# Drell-Yan to 2Mu, amcatnlo
#

# cpn.add_dataset(
#     name="dy_mumu_m50toinf_amcatnlo",
#     id=490076405,
#     processes=[procs.dy_mumu_m50],
#     keys=[
#         "/DYto2Mu-2Jets_Bin-MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v6/NANOAODSIM",  # noqa
#     ],
#     n_files=2975,
#     n_events=490076405,
# )

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

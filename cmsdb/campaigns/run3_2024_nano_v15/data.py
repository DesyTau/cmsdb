# coding: utf-8

"""
Recorded datasets for the 2024 data-taking campaign with datasets at NanoAOD tier in version 15.
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2024_nano_v15 import campaign_run3_2024_nano_v15 as cpn

# EGamma

cpn.add_dataset(
    name="data_egamma_C",
    id=157351226 + 157860731,
    is_data=True,
    processes=[procs.data_egamma],
    keys=[
        "/EGamma0/Run2024C-MINIv6NANOv15-v1/NANOAOD",
        "/EGamma1/Run2024C-MINIv6NANOv15-v1/NANOAOD",
    ],
    n_files=167 + 247,
    n_events=157351226 + 157860731,
    aux={
        "era": "C",
    },
) 

cpn.add_dataset(
    name="data_egamma_D",
    id=156558757 + 156275778,
    is_data=True,
    processes=[procs.data_egamma],
    keys=[
        "/EGamma0/Run2024D-MINIv6NANOv15-v1/NANOAOD",
        "/EGamma1/Run2024D-MINIv6NANOv15-v1/NANOAOD",
    ],
    n_files=173 + 279,
    n_events=156558757 + 156275778,
    aux={
        "era": "D",
    },
) 

cpn.add_dataset(
    name="data_egamma_E",
    id=249417634 + 249489829,
    is_data=True,
    processes=[procs.data_egamma],
    keys=[
        "/EGamma0/Run2024E-MINIv6NANOv15-v1/NANOAOD",
        "/EGamma1/Run2024E-MINIv6NANOv15-v1/NANOAOD",
    ],
    n_files=267 + 335,
    n_events=249417634 + 249489829,
    aux={
        "era": "E",
    },
) 

cpn.add_dataset(
    name="data_egamma_F",
    id=638196622 + 631079889,
    is_data=True,
    processes=[procs.data_egamma],
    keys=[
        "/EGamma0/Run2024F-MINIv6NANOv15-v1/NANOAOD",
        "/EGamma1/Run2024F-MINIv6NANOv15-v1/NANOAOD",
    ],
    n_files=719 + 747,
    n_events=638196622 + 631079889,
    aux={
        "era": "F",
    },
)

cpn.add_dataset(
    name="data_egamma_G",
    id=903520258 + 903441926,
    is_data=True,
    processes=[procs.data_egamma],
    keys=[
        "/EGamma0/Run2024G-MINIv6NANOv15-v2/NANOAOD",
        "/EGamma1/Run2024G-MINIv6NANOv15-v2/NANOAOD",
    ],
    n_files=850 + 888,
    n_events=903520258 + 903441926,
    aux={
        "era": "G",
    },
)

cpn.add_dataset(
    name="data_egamma_H",
    id=134680448 + 134835799,
    is_data=True,
    processes=[procs.data_egamma],
    keys=[
        "/EGamma0/Run2024H-MINIv6NANOv15-v2/NANOAOD",
        "/EGamma1/Run2024H-MINIv6NANOv15-v1/NANOAOD",
    ],
    n_files=138 + 191,
    n_events=134680448 + 134835799,
    aux={
        "era": "H",
    },
)

cpn.add_dataset(
    name="data_egamma_I",
    id=132904290 + 132903874,
    is_data=True,
    processes=[procs.data_egamma],
    keys=[
        "/EGamma0/Run2024I-MINIv6NANOv15-v1/NANOAOD",
        "/EGamma1/Run2024I-MINIv6NANOv15-v1/NANOAOD",
    ],
    n_files=211 + 176,
    n_events=132904290 + 132903874,
    aux={
        "era": "I",
    },
)


# Muon

cpn.add_dataset(
    name="data_mu_C",
    id=195037585,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/Muon0/Run2024C-MINIv6NANOv15-v1/NANOAOD",
        "/Muon1/Run2024C-MINIv6NANOv15-v1/NANOAOD",
    ],
    n_files=103 + 94,
    n_events=97505587 + 97531998,
    aux={
        "prompt": False,
        "era": "C",
    },
)

cpn.add_dataset(
    name="data_mu_D",
    id=241254436,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/Muon0/Run2024D-MINIv6NANOv15-v1/NANOAOD",
        "/Muon1/Run2024D-MINIv6NANOv15-v1/NANOAOD",
    ],
    n_files=180 + 168,
    n_events=120787065 + 120467371,
    aux={
        "prompt": False,
        "era": "D",
    },
)

cpn.add_dataset(
    name="data_mu_E",
    id=342489620,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/Muon0/Run2024E-MINIv6NANOv15-v1/NANOAOD",
        "/Muon1/Run2024E-MINIv6NANOv15-v1/NANOAOD",
    ],
    n_files=255 + 171,
    n_events=169640946 + 172848674,
    aux={
        "prompt": False,
        "era": "E",
    },
)

cpn.add_dataset(
    name="data_mu_F",
    id=884793210,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/Muon0/Run2024F-MINIv6NANOv15-v1/NANOAOD",
        "/Muon1/Run2024F-MINIv6NANOv15-v1/NANOAOD",
    ],
    n_files=594 + 538,
    n_events=442432787 + 442360423,
    aux={
        "prompt": True,
        "era": "F",
    },
)

cpn.add_dataset(
    name="data_mu_G",
    id=1283988446,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/Muon0/Run2024G-MINIv6NANOv15-v1/NANOAOD",
        "/Muon1/Run2024G-MINIv6NANOv15-v2/NANOAOD",
    ],
    n_files=948 + 565,
    n_events=642028803 + 641959643,
    aux={
        "prompt": True,
        "era": "G",
    },
)

cpn.add_dataset(
    name="data_mu_H",
    id=187964729,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/Muon0/Run2024H-MINIv6NANOv15-v1/NANOAOD",
        "/Muon1/Run2024H-MINIv6NANOv15-v2/NANOAOD",
    ],
    n_files=152 + 93,
    n_events=93983627 + 93981102,
    aux={
        "prompt": True,
        "era": "H",
    },
)

cpn.add_dataset(
    name="data_mu_I",
    id=405647781,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/Muon0/Run2024I-MINIv6NANOv15-v1/NANOAOD",
        "/Muon1/Run2024I-MINIv6NANOv15-v1/NANOAOD",
        "/Muon0/Run2024I-MINIv6NANOv15_v2-v1/NANOAOD",
        "/Muon1/Run2024I-MINIv6NANOv15_v2-v1/NANOAOD",
    ],
    n_files=173 + 94 + 174 + 133,
    n_events=97634104 + 97630010 + 105194627 + 105189040,
    aux={
        "prompt": True,
        "era": "I",
    },
)
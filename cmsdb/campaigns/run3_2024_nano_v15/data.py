# coding: utf-8

"""
Recorded datasets for the 2024 data-taking campaign with datasets at NanoAOD tier in version 15.
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2024_nano_v15 import campaign_run3_2024_nano_v15 as cpn

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
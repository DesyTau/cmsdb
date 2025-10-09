# coding: utf-8

__all__ = [  
"vv","zz", "ww", "wz",
]


from order import Process
from scinum import Number

import cmsdb.constants as const

#
# Di-boson
#

vv = Process(
    name="vv",
    id=8000,
    label="Di-Boson",
    color="#80cdc1",
)

# # ZZ 13 TeV xsec values at nNNLO from
# zz = vv.add_process(
#     name="zz",
#     id=8100,
#     label="ZZ",
#     xsecs={
#         13.6: Number(24.97, {"scale": (0.029j, 0.027j)}) * (12.75 / 12.14),
#     },
#     color="#01665e",
# )

# ww = vv.add_process(
#     name="ww",
#     id=8300,
#     label="WW",
#     xsecs={
#         13.6: Number(80.22, {
#             "tot": 0.01677,  # xsdb: Number(80.23, {"tot": 0.3733})
#         }),
#     },
#     color="#c7eae5",
# )

# wz = vv.add_process(
#     name="wz",
#     id=8200,
#     label="WZ",
#     xsecs={
#         13.6: Number(29.17, {
#             "tot": 0.005941,  # xsdb: Number(29.1, {"tot": 0.1318}),
#         }),
#     },
#     color="#5ab4ac",
# )

# ZZ 13 TeV xsec values at nNNLO from
zz = vv.add_process(
    name="zz",
    id=8100,
    label="ZZ",
    xsecs={
        13.6: Number(19.431)
    },
    color="#01665e",
)

ww = vv.add_process(
    name="ww",
    id=8300,
    label="WW",
    xsecs={
        13.6: Number(122.27052),
    },
    color="#c7eae5",
)

wz = vv.add_process(
    name="wz",
    id=8200,
    label="WZ",
    xsecs={
        13.6: Number(41.1474),
    },
    color="#5ab4ac",
)
# coding: utf-8

__all__ = [  
"dy_ll","dy_m50toinf", "dy_m10to50", "dy_m50toinf_0j", "dy_m50toinf_1j", "dy_m50toinf_2j",
]


from order import Process
from scinum import Number

import cmsdb.constants as const

dy_ll = Process(
    name="dy_ll",
    id=20950+6282+5378+973+312,
    label="Z/γ*→ll",
    color="#b2d99a"
)

# dy_m10to50 = dy_ll.add_process(
#     name="dy_m10to50",
#     id=20950,
#     xsecs={13.6: 20950.0},
#     color="#c6dbef",
#     aux={
#         "mll": (10.0, 50.0),
#     },
# )
# dy_m50toinf = dy_ll.add_process(
#     name="dy_m50toinf",
#     id=6282,
#     xsecs={
#         13.6: Number(6282.6, {
#             "scale": (0.008j, 0.013j),
#             "pdf": 0.01j,
#         }),
#     },
#     color="#08519c",
#     aux={
#         "mll": (50.0, const.inf),
#     },
# )
# dy_m50toinf_0j = dy_ll.add_process(
#     name="dy_m50toinf_0j",
#     id=5378,
#     xsecs={
#         13.6: Number(5378, 
#         {"tot": 8.007}),
#     },
#     color="#9ecae1",
#     aux={
#         "mll": (50.0, const.inf),
#         "njets": (0, 1),
#     },
# )

# dy_m50toinf_1j = dy_ll.add_process(
#     name="dy_m50toinf_1j",
#     id=973,
#     xsecs={
#         13.6: Number(973.1,
#             {"tot": 2.613}),
#     },
#     color="#4292c6",
#     aux={
#         "mll": (50.0, const.inf),
#         "njets": (1, 2),
#     },
# )

# dy_m50toinf_2j = dy_ll.add_process(
#     name="dy_m50toinf_2j",
#     id=312,
#     xsecs={
#         13.6: Number(312.4, 
#         {"tot": 0.915}),
#     },
#     color="#2171b5",
#     aux={
#         "mll": (50.0, const.inf),
#         "njets": (2, 3),
#     },
# )

dy_m10to50 = dy_ll.add_process(
    name="dy_m10to50",
    id=20950,
    xsecs={13.6: 20950.0},
    color="#c6dbef",
    aux={
        "mll": (10.0, 50.0),
    },
)
dy_m50toinf = dy_ll.add_process(
    name="dy_m50toinf",
    id=6282,
    xsecs={
        13.6: Number(6748.0, {
            "scale": (0.008j, 0.013j),
            "pdf": 0.01j,
        }),
    },
    color="#08519c",
    aux={
        "mll": (50.0, const.inf),
    },
)
dy_m50toinf_0j = dy_ll.add_process(
    name="dy_m50toinf_0j",
    id=5378,
    xsecs={
        13.6: Number(5364, 
        {"tot": 8.007}),
    },
    color="#9ecae1",
    aux={
        "mll": (50.0, const.inf),
        "njets": (0, 1),
    },
)

dy_m50toinf_1j = dy_ll.add_process(
    name="dy_m50toinf_1j",
    id=973,
    xsecs={
        13.6: Number(1019.0,
            {"tot": 2.613}),
    },
    color="#4292c6",
    aux={
        "mll": (50.0, const.inf),
        "njets": (1, 2),
    },
)

dy_m50toinf_2j = dy_ll.add_process(
    name="dy_m50toinf_2j",
    id=312,
    xsecs={
        13.6: Number(375.3, 
        {"tot": 0.915}),
    },
    color="#2171b5",
    aux={
        "mll": (50.0, const.inf),
        "njets": (2, 3),
    },
)

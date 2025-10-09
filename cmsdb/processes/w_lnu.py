# coding: utf-8

__all__ = [  
"w_lnu","w_lnu_0j", "w_lnu_1j", "w_lnu_2j",
]


from order import Process
from scinum import Number

import cmsdb.constants as const

w_lnu = Process(
    name="w_lnu",
    id=6100,
    label=rf"$W \rightarrow l\nu$",
    xsecs={13.6: 63425.1},
    color="#74c476",
)

w_lnu_0j = w_lnu.add_process(
    name="w_lnu_0j",
    id=610000,
    label=rf"$W \rightarrow l\nu$ 0j",
    aux={
        "njets": (0, 1),
    },
)

w_lnu_1j = w_lnu.add_process(
    name="w_lnu_1j",
    id=610010,
    label=rf"$W \rightarrow l\nu$ 1j",
    color="#31a354",
    aux={
        "njets": (1, 2),
    },
)

w_lnu_2j = w_lnu.add_process(
    name="w_lnu_2j",
    id=610020,
    label=rf"$W \rightarrow l\nu$ 2j",
    color="#238b45",
    aux={
        "njets": (2, 3),
    },
)
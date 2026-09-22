# coding: utf-8

from __future__ import annotations

__all__ = [
    "ggphi_phitt","bbphi_phitt"
]


from order import Process
from scinum import Number
import sys

from cmsdb.util import add_xsecs, DotDict, add_decay_process, add_sub_decay_process

# grab a reference to this module so we can attach new names to it
this_module = sys.modules[__name__]


ggphi_phitt = Process(
    name="ggphi_phitt",
    id=2223240,
    label=r"$gg\phi \rightarrow \tau\tau$",
    xsecs={
        13: Number(1.0),
        13.6: Number(1.0),  
    },
)
bbphi_phitt = Process(
    name="bbphi_phitt",
    id=2223241,
    label=r"$bb\phi \rightarrow \tau\tau$",
    xsecs={
        13: Number(1.0),
        13.6: Number(1.0),  
    },
)

signal_masses = [60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 160, 180, 200, 250, 300, 350, 400, 450, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1400, 1600, 1800, 2000, 2300, 2600, 2900, 3200, 3500]

for mass in signal_masses:
    proc = ggphi_phitt.add_process(
        name=f"ggphi_phitt_{mass}",
        id=mass+10**8,
        xsecs={
            13: Number(1.0),
            13.6: Number(1.0),  
        },
    )
    
    proc = bbphi_phitt.add_process(
            name=f"bbphi_phitt_{mass}",
            id=mass+1+10**8,
            xsecs={
                13: Number(1.0),
                13.6: Number(1.0),  
            },
    )
    setattr(this_module, f"bbphi_phitt_{mass}", proc)
    setattr(this_module, f"ggphi_phitt_{mass}", proc)

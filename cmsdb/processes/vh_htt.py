# coding: utf-8
from __future__ import annotations

__all__ = [
    "vh_htt","w_plus_h_htt_UU","w_minus_h_htt_UU","zh_htt_UU",
]

from order import Process
from scinum import Number

import cmsdb.constants as const
from cmsdb.util import add_xsecs, DotDict, add_decay_process, add_sub_decay_process

####################################################################################################
#
# WH subprocesses
#
####################################################################################################

vh_htt = Process(
    name="vh_htt",
    id=16100,
    label="VH",
    xsecs={13.6: Number(0.1)},  
    color="#f768a1"
)

# Higgs decay channels
w_plus_h_htt_UU = vh_htt.add_process(
    name="w_plus_h_htt_UU",
    id=16101,
    xsecs={
        13.6: Number(0.05575),
    },
   color="#f768a1", 
)

w_minus_h_htt_UU = vh_htt.add_process(
    name="w_minus_h_htt_UU",
    id=16102,
    xsecs={
        13.6: Number(0.03561),
    },
   color="#f768a1", 
)
zh_htt_UU = vh_htt.add_process(
    name="zh_htt_UU",
    id=16103,
    xsecs={
        13.6: Number(0.0592),
    },
   color="#ce1256"
)

# import csv

# # Your target list
# process_names = [
#     # vh_htt
#     "vh_htt",
#     "zh_htt_UU",
#     "w_plus_h_htt_UU",
#     "w_minus_h_htt_UU",
# ]

# def _is_process(obj) -> bool:
#     # duck-typing for order.Process
#     return hasattr(obj, "name") and hasattr(obj, "get_xsec") and hasattr(obj, "xsecs")

# def _to_float(x):
#     """Plain float from scinum.Number or numeric; None if unavailable."""
#     try:
#         return float(x)
#     except Exception:
#         for attr in ("nominal", "n", "value", "val"):
#             if hasattr(x, attr):
#                 try:
#                     return float(getattr(x, attr))
#                 except Exception:
#                     pass
#     return None

# energy = 13.6
# out_path = "used_xsecs.txt"

# # Build registry from module globals
# proc_map = {obj.name: obj for obj in globals().values() if _is_process(obj)}

# # Collect rows
# rows = []
# for pname in process_names:
#     p = proc_map.get(pname)
#     if p is None:
#         rows.append([pname, None, "Process not found"])
#         continue
#     try:
#         v = p.get_xsec(energy)  # may raise if energy not present
#     except Exception:
#         v = None
#     rows.append([pname, _to_float(v) if v is not None else None, ""])

# # Write TSV
# header = ["process", "xsec_13.6TeV_pb", "note"]
# with open(out_path, "a", newline="") as f:
#     w = csv.writer(f, delimiter="\t")
#     w.writerow(header)
#     w.writerows(rows)

# print(f"Wrote {len(rows)} rows -> {out_path}")
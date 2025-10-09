# coding: utf-8

__all__ = [  
"vvv","zzz", "www", "wwz", "wzz",
]


from order import Process
from scinum import Number

import cmsdb.constants as const


#
# Triple-boson
#

vvv = Process(
    name="vvv",
    id=9000,
    label="Triple-Boson",
    # xsecs set below as sum over individual processes
    color="#bdbdbd",
)

# based on GenXSecAnalyzer
# for ZZZ_TuneCP5_13TeV-amcatnlo-pythia8 (Summer20UL16, NLO)
# remark: calculated xsec has lower error for sample without ext-1 as not all events were used for calculation of ext-1
# therefore the value for the sample without ext-1 is taken
# using command ./calculateXSectionAndFilterEfficiency.sh -f datasets.txt -c RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1 -n 5000000  # noqa
zzz = vvv.add_process(
    name="zzz",
    id=9100,
    xsecs={
        13: Number(0.01476, {"tot": 2.347 * 10**(-6)}),
        # 13.6 from GenXSecAnalyzer:
        # similar values also found in http://cms.cern.ch/iCMS/jsp/openfile.jsp?tp=draft&files=AN2023_179_v6.pdf
        # same value as xsdb obtained
        13.6: Number(0.01591, {
            "tot": 0.000007828,
        }),
    },
    color="#525252"
)

# based on GenXSecAnalyzer
# for WZZ_TuneCP5_13TeV-amcatnlo-pythia8 (Summer20UL16, NLO, ext-1)
# remark: calculated xsec is the same for simple sample and ext-1 sample
# using command ./calculateXSectionAndFilterEfficiency.sh -f datasets.txt -c RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17_ext1-v1 -n 5000000  # noqa
wzz = vvv.add_process(
    name="wzz",
    id=9200,
    xsecs={
        13: Number(0.05709, {"tot": 6.213 * 10**(-5)}),
        # 13.6 from GenXSecAnalyzer:
        # similar values also found in http://cms.cern.ch/iCMS/jsp/openfile.jsp?tp=draft&files=AN2023_179_v6.pdf
        # same value as xsdb obtained
        13.6: Number(0.06206, {
            "tot": 0.00003689,
        }),
    },
)

# based on GenXSecAnalyzer
# for WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8 (Summer20UL16, NLO, ext-1)
# remark: calculated xsec is the same for simple sample and ext-1 sample
# using command ./calculateXSectionAndFilterEfficiency.sh -f datasets.txt -c RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17_ext1-v1 -n 5000000  # noqa
wwz = vvv.add_process(
    name="wwz",
    id=9300,
    xsecs={
        13: Number(0.1707, {"tot": 0.0001757}),
        # 13.6 from GenXSecAnalyzer:
        # similar values also found in http://cms.cern.ch/iCMS/jsp/openfile.jsp?tp=draft&files=AN2023_179_v6.pdf
        # same value as xsdb obtained
        13.6: Number(0.1851, {
            "tot": 0.00009482,
        }),
    },
    color="#737373",
)

# based on GenXSecAnalyzer
# for WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8 (Summer20UL16, NLO, ext-1)
# remark: calculated xsec is the same for simple sample and ext-1 sample
# using command ./calculateXSectionAndFilterEfficiency.sh -f datasets.txt -c RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17_ext1-v1 -n 5000000  # noqa
www = vvv.add_process(
    name="www",
    id=9400,
    xsecs={
        13: Number(0.2158, {"tot": 0.0002479}),
        # 13.6 from GenXSecAnalyzer:
        # similar values also found in http://cms.cern.ch/iCMS/jsp/openfile.jsp?tp=draft&files=AN2023_179_v6.pdf
        # same value as xsdb obtained
        13.6: Number(0.2328, {
            "tot": 0.0001247,
        }),
    },
    color="#969696",
)

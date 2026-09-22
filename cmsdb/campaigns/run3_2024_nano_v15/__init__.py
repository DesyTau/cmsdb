from order import Campaign

#
# campaign
#

campaign_run3_2024_nano_v15 = Campaign(
    name="run3_2024_nano_v15",
    id=32024151,  # (run)3(year)2024(version)15(random number)1
    ecm=13.6,
    bx=25,
    aux={
        "tier": "NanoAOD",
        "run": 3,
        "year": 2024,
        "version": 15,
        "tag": "2024",
        "postfix" : "",
        "custom": {},
    },
)

import cmsdb.campaigns.run3_2024_nano_v15.data  # noqa
import cmsdb.campaigns.run3_2024_nano_v15.top  # noqa
import cmsdb.campaigns.run3_2024_nano_v15.ewk  # noqa
import cmsdb.campaigns.run3_2024_nano_v15.cp_signal  # noqa
import cmsdb.campaigns.run3_2024_nano_v15.signal  # noqa
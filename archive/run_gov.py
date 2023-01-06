import pandas as pd

# Modules
from pkg_gov.whitehouse import *
from pkg_gov.supremecourt import *
from pkg_gov.congress import *

from pkg_gov.irs import *
from pkg_gov.agriculture import *
from pkg_gov.commerce import *
from pkg_gov.defense import *
from pkg_gov.ed import *
from pkg_gov.energy import *
from pkg_gov.hhs import *
from pkg_gov.homeland import *
from pkg_gov.hud import *
from pkg_gov.interior import *
from pkg_gov.justice import *
from pkg_gov.labor import *
from pkg_gov.state import *
from pkg_gov.transportation import *
from pkg_gov.treasury import *
from pkg_gov.va import *

def gov_scrape():
    combined_df = pd.DataFrame()
    
    combined_df = combined_df.append(whitehouse_scrape())
    combined_df = combined_df.append(supremecourt_scrape())
    combined_df = combined_df.append(congress_scrape())
    combined_df = combined_df.append(agriculture_scrape())
    combined_df = combined_df.append(irs_scrape())
    combined_df = combined_df.append(commerce_scrape())
    combined_df = combined_df.append(defense_scrape())
    combined_df = combined_df.append(ed_scrape())
    combined_df = combined_df.append(energy_scrape())
    combined_df = combined_df.append(hhs_scrape())
    combined_df = combined_df.append(homeland_scrape())
    combined_df = combined_df.append(hud_scrape())
    combined_df = combined_df.append(interior_scrape())
    combined_df = combined_df.append(justice_scrape())
    combined_df = combined_df.append(labor_scrape())
    combined_df = combined_df.append(state_scrape())
    combined_df = combined_df.append(transportation_scrape())
    combined_df = combined_df.append(treasury_scrape())
    combined_df = combined_df.append(va_scrape())
    #print(combined_df)
    gov_df = combined_df

    print("Gov DF: ")
    print(gov_df)
    gov_df.to_csv(r'gov_data.csv',index=False)
    return gov_df

gov_scrape()
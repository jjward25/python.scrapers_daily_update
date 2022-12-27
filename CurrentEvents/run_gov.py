from bs4 import BeautifulSoup  ## BeautifulSoup is a web parsing package to help pull specific HTML components
from datetime import date
import pandas as pd

# Modules
from gov.whitehouse import *
from gov.supremecourt import *
from gov.congress import *

from gov.irs import *
from gov.agriculture import *
from gov.commerce import *
from gov.defense import *
from gov.ed import *
from gov.energy import *
from gov.hhs import *
from gov.homeland import *
from gov.hud import *
#from gov.interior import *
from gov.justice import *
from gov.labor import *
#from gov.state import *
from gov.transportation import *
from gov.treasury import *
from gov.va import *

combined_df = pd.DataFrame()

def gov_scrape():
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
    #combined_df = combined_df.append(interior_scrape())
    combined_df = combined_df.append(justice_scrape())
    combined_df = combined_df.append(labor_scrape())
    #combined_df = combined_df.append(state_scrape())
    combined_df = combined_df.append(transportation_scrape())
    combined_df = combined_df.append(treasury_scrape())
    combined_df = combined_df.append(va_scrape())
    #print(combined_df)

    gov_df = combined_df
    print(gov_df)
    gov_df.to_csv(r'gov_data.csv',index=False)
    return gov_df
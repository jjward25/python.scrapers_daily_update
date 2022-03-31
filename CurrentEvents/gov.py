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

white_house_df = whitehouse_scrape()
supreme_court_df = supremecourt_scrape()
congress_df = congress_scrape()
irs_df = irs_scrape()

agriculture_dept_df = agriculture_scrape()
commerce_dept_df = commerce_scrape()
defense_dept_df = defense_scrape()
ed_dept_df = ed_scrape()
energy_dept_df = energy_scrape()
hhs_dept_df = hhs_scrape()
homeland_dept_df = homeland_scrape()
hud_dept_df = hud_scrape()
#interior_dept_df = interior_scrape()
justice_dept_df = justice_scrape()
labor_dept_df = labor_scrape()
#state_dept_df = state_scrape()
transportation_dept_df = transportation_scrape()
treasury_dept_df = treasury_scrape()
va_dept_df = va_scrape()

combined_df = pd.DataFrame()
combined_df = combined_df.append(agriculture_dept_df)
combined_df = combined_df.append(white_house_df)
combined_df = combined_df.append(supreme_court_df)
combined_df = combined_df.append(congress_df)
combined_df = combined_df.append(irs_df)
combined_df = combined_df.append(commerce_dept_df)
combined_df = combined_df.append(defense_dept_df)
combined_df = combined_df.append(ed_dept_df)
combined_df = combined_df.append(energy_dept_df)
combined_df = combined_df.append(hhs_dept_df)
combined_df = combined_df.append(homeland_dept_df)
combined_df = combined_df.append(hud_dept_df)
#combined_df = combined_df.append(interior_dept_df)
combined_df = combined_df.append(justice_dept_df)
combined_df = combined_df.append(labor_dept_df)
#combined_df = combined_df.append(state_dept_df)
combined_df = combined_df.append(transportation_dept_df)
combined_df = combined_df.append(treasury_dept_df)
combined_df = combined_df.append(va_dept_df)
#print(combined_df)

gov_df = combined_df
print(gov_df)
gov_df.to_csv(r'gov_data.csv',index=False)
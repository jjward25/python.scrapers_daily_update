from bs4 import BeautifulSoup  ## BeautifulSoup is a web parsing package to help pull specific HTML components
from datetime import date
import pandas as pd


from pkg_gov.agriculture import *
from pkg_gov.commerce import *
from pkg_gov.congress import *
from pkg_gov.defense import *
from pkg_gov.ed import *
from pkg_gov.energy import *
from pkg_gov.hhs import *
from pkg_gov.homeland import *
from pkg_gov.interior import *
from pkg_gov.irs import *
from pkg_gov.justice import *
from pkg_gov.labor import *
from pkg_gov.state import *
from pkg_gov.supremecourt import *
from pkg_gov.transportation import *
from pkg_gov.treasury import *
from pkg_gov.va import *
from pkg_gov.whitehouse import *
from pkg_gov.hud import *


#combine all files in the list
gov_list = [agriculture_df,commerce_dept_df,congress_df,defense_df,education_df,energy_df,hhs_df,homeland_df,hud_df,interior_df,irs_df,justice_df,labor_df,state_df,supreme_court_df,transportation_df,treasury_df,va_df,white_house_df]

gov_df = pd.concat(gov_list)
#print(combined_df)
print(gov_df)
gov_df.to_csv(r'gov.csv',index=False)
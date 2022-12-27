from bs4 import BeautifulSoup  ## BeautifulSoup is a web parsing package to help pull specific HTML components
from datetime import date
import pandas as pd

# Modules
from headlines.apbusiness import *
from headlines.aphealth import *



combined_df = pd.DataFrame()
combined_df = combined_df.append(apbiz_scrape())
combined_df = combined_df.append(aphealth_scrape())

#print(combined_df)

opeds_df = combined_df
print(opeds_df)
opeds_df.to_csv(r'opeds.csv',index=False)
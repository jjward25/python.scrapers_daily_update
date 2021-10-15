from bs4 import BeautifulSoup  ## BeautifulSoup is a web parsing package to help pull specific HTML components
import urllib.request  ## to get a access to a URL and its content
import csv
from datetime import date
import pandas as pd

# Modules
from sites.nationalreview import national_review_df
from sites.politico import politico_df
from sites.cfr import cfr_df
from sites.nyt import nyt_df

from sites.apbusiness import apbiz_df
from sites.aphealth import aphealth_df
from sites.appolitics import appolitics_df
from sites.apscience import apscience_df
from sites.aptech import aptech_df
from sites.apus import apus_df
from sites.apworld import apworld_df

from sites.reuters_biz import reuters_biz_df
from sites.reuters_breaking import reuters_breaking_df
from sites.reuters_legal import reuters_legal_df
from sites.reuters_tech import reuters_tech_df
from sites.reuters_world import reuters_world_df

combined_df = pd.DataFrame()
combined_df = combined_df.append(national_review_df)
combined_df = combined_df.append(politico_df)
combined_df = combined_df.append(cfr_df)
combined_df = combined_df.append(nyt_df)

combined_df = combined_df.append(apus_df)
combined_df = combined_df.append(apworld_df)
combined_df = combined_df.append(apbiz_df)
combined_df = combined_df.append(aphealth_df)
combined_df = combined_df.append(appolitics_df)
combined_df = combined_df.append(apscience_df)
combined_df = combined_df.append(aptech_df)

combined_df = combined_df.append(reuters_biz_df)
combined_df = combined_df.append(reuters_breaking_df)
combined_df = combined_df.append(reuters_legal_df)
combined_df = combined_df.append(reuters_tech_df)
combined_df = combined_df.append(reuters_world_df)
#print(combined_df)

headlines_df = combined_df
#print(headlines_df)
headlines_df.to_csv(r'headlines.csv', index=False)
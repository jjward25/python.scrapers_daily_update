from bs4 import BeautifulSoup  ## BeautifulSoup is a web parsing package to help pull specific HTML components
from datetime import date
import pandas as pd

from pkg_headlines.appolitics import *
from pkg_headlines.apus import *
from pkg_headlines.apworld import *
from pkg_headlines.nyt import *
from pkg_headlines.politico import *
from pkg_headlines.reuters_breaking import *
from pkg_headlines.reuters_legal import *
from pkg_headlines.reuters_world import *


#combine all files in the list
df_list = [appolitics_df,apus_df,apworld_df,nyt_selenium_df,politico_df,reuters_breaking_df,reuters_legal_df,reuters_world_df]
headlines_df = pd.concat(df_list)
#print(combined_df)
print(headlines_df)
headlines_df.to_csv(r'headlines.csv',index=False)
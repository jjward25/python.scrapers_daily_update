from bs4 import BeautifulSoup  ## BeautifulSoup is a web parsing package to help pull specific HTML components
from datetime import date
import pandas as pd

from pkg_stembiz.apbusiness import *
from pkg_stembiz.aphealth import *
from pkg_stembiz.apscience import *
from pkg_stembiz.aptech import *
from pkg_stembiz.arstechnica import *
from pkg_stembiz.bloomberg import *
from pkg_stembiz.economist import *
from pkg_stembiz.reuters_biz import *
from pkg_stembiz.reuters_tech import *
from pkg_stembiz.scientific_american import *

#combine all files in the list
df_list = [apbiz_df,aphealth_df,apscience_df,aptech_df,ars_df,bloomberg_df,reuters_biz_df,reuters_tech_df,scientific_american_df]
stembiz_df = pd.concat(df_list)
#print(combined_df)
print(stembiz_df)
stembiz_df.to_csv(r'stembiz.csv',index=False)
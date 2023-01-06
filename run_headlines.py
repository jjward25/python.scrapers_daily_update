from bs4 import BeautifulSoup  ## BeautifulSoup is a web parsing package to help pull specific HTML components
from datetime import date
import pandas as pd


from pkg_headlines.politico import *
from pkg_headlines.reuters_biz import *
from pkg_headlines.reuters_tech import *
from pkg_headlines.reuters_world import *


#combine all files in the list
df_list = [politico_df,reuters_biz_df,reuters_tech_df,reuters_world_df]
headlines_df = pd.concat(df_list)
#print(combined_df)
print(headlines_df)
headlines_df.to_csv(r'headlines.csv',index=False)
from bs4 import BeautifulSoup  ## BeautifulSoup is a web parsing package to help pull specific HTML components
from datetime import date
import pandas as pd


from pkg_opeds.cfr import *
from pkg_opeds.foreignaffairs import *
from pkg_opeds.jacobin import *
from pkg_opeds.nationalreview import *
from pkg_opeds.stratechery import *
from pkg_opeds.sinocism import *


#combine all files in the list
df_list = [cfr_df, foreign_affairs_df, jacobin_df, national_review_df, stratechery_df, sinocism_df]
opeds_df = pd.concat(df_list)
#print(combined_df)
print(opeds_df)
opeds_df.to_csv(r'opeds.csv',index=False)
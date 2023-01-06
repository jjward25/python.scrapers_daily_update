from bs4 import BeautifulSoup  ## BeautifulSoup is a web parsing package to help pull specific HTML components
from datetime import date
import pandas as pd


from pkg_stembiz.arstechnica import *

#combine all files in the list
df_list = [ars_df]
stembiz_df = pd.concat(df_list)
#print(combined_df)
print(stembiz_df)
stembiz_df.to_csv(r'stembiz.csv',index=False)
from bs4 import BeautifulSoup  ## BeautifulSoup is a web parsing package to help pull specific HTML components
from datetime import date
import pandas as pd

# Modules
#from headlines.apbusiness import *
#from headlines.aphealth import *
#from headlines.appolitics import *
#from headlines.apscience import *
#from headlines.aptech import *
#from headlines.apus import *
#from headlines.nyt import *
#from headlines.politico import *
from headlines.reuters_biz import *
#from headlines.reuters_breaking import *
#from headlines.reuters_legal import *
from headlines.reuters_tech import *
from headlines.reuters_world import *


#apbiz_df = apbiz_scrape()
#aphealth_df = aphealth_scrape()
#appolitics_df = appolitics_scrape()



def headline_scrape():
    combined_df = pd.DataFrame()
    
    #combined_df = combined_df.append(apbiz_scrape())
    #combined_df = combined_df.append(aphealth_scrape())
    #combined_df = combined_df.append(appolitics_scrape())
    #combined_df = combined_df.append(apscience_scrape())
    #combined_df = combined_df.append(aptech_scrape())
    ##combined_df = combined_df.append(apus_scrape())
    #combined_df = combined_df.append(nyt_scrape())
    #combined_df = combined_df.append(politico_scrape())
    combined_df = combined_df.append(reutersbiz_scrape())
    #combined_df = combined_df.append(reutersbreaking_scrape())
    #combined_df = combined_df.append(reuterslegal_scrape())
    combined_df = combined_df.append(reuterstech_scrape())
    combined_df = combined_df.append(reutersworld_scrape())

    #print(combined_df)

    headlines_df = combined_df
    print(headlines_df)
    headlines_df.to_csv(r'headline_data.csv',index=False)
    return headlines_df

headline_scrape()
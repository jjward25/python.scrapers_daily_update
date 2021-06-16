from bs4 import BeautifulSoup  ## BeautifulSoup is a web parsing package to help pull specific HTML components
import urllib.request  ## to get a access to a URL and its content
import csv
from datetime import date
import pandas as pd

# Modules
from gov_pkg.gov import gov_df
from oped_pkg.oped import oped_df


combined_df = pd.DataFrame()
combined_df = combined_df.append(gov_df)
combined_df = combined_df.append(oped_df)
#print(combined_df)

current_events_df = combined_df
print(current_events_df)
current_events_df.to_csv(r'C:\Users\Josep\OneDrive\Desktop\Coding\CA Scrapers\Current Events\current_events_data.csv')
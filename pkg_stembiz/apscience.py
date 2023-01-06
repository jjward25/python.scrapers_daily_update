from bs4 import BeautifulSoup  ## BeautifulSoup is a web parsing package to help pull specific HTML components
import urllib.request  ## to get a access to a URL and its content
import pandas as pd 
from datetime import date, timedelta, datetime
import requests 

## Date List created with string values for the last 4 days to only pull opinions from that range.  
## General templates to pull from, not all are always used.
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.46'}
link = "https://apnews.com/hub/science?utm_source=apnewsnav&utm_medium=navigation"

##** Error Handling for bad URL
try:
    page = requests.get(link, headers=headers)
    page.raise_for_status()
except:
    print('URL Broken')
    obj_list = [{'type':'Headline','source':'AP Science', 'title': 'Link Broken', 'link': '', 'Notes': '', 'date': ''}]
    apscience_df = pd.DataFrame(obj_list)
    
## Parse the webpage
page = requests.get(link, headers=headers)
soup = BeautifulSoup(page.content, 'lxml')


## Actual HTML pull
object_list = []
for item in soup.find_all(class_='CardHeadline')[0:7]:
#if item.find('span').get_text() in date_list:
    title = item.find('a').find('h2').get_text()
    ilink = "https://www.apnews.com" + str(item.find('a').get('href'))
    #notes = item.find(class_='summary f-serif ls-0').get_text()
    #idate = item.find(class_='publication-date').get_text()

    obj_data = {'type':'Headline','source':'AP Science', 'title': title, 'link': ilink, 'Notes': 'notes', 'date': 'idate'}
    object_list.append(obj_data)

## Final dataframe is defined
apscience_df = pd.DataFrame(object_list).head(8)

##** Error Handling for empty result
if len(apscience_df) == 0:
    print('No Result')
    obj_list = [{'type':'Headline','source':'AP Science', 'title': 'Data List Empty', 'link': '', 'Notes': '', 'date': ''}]
    apscience_df = pd.DataFrame(obj_list)
    
## Final Return Statement
print(apscience_df)

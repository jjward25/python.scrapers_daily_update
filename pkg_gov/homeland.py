from bs4 import BeautifulSoup  ## BeautifulSoup is a web parsing package to help pull specific HTML components
import pandas as pd 
from datetime import date, timedelta, datetime
import requests 

## Date List created with string values for the last 4 days to only pull opinions from that range.  
## General templates to pull from, not all are always used.
today = date.today()
yesterday = date.today() - timedelta(1)
today_date = today.strftime("%Y-%m-%d")
yesterday_date = yesterday.strftime("%Y-%m-%d")
today_word = today.strftime("%B %d, %Y")
today_word_single_digit_day = today.strftime("%B %d, %Y").replace(" 0", " ")
yesterday_word = yesterday.strftime("%B %d, %Y")
yesterday_word_single_digit_day = yesterday.strftime("%B %d, %Y").replace(" 0", " ")
date_list = [today_date,yesterday_date,today_word,yesterday_word,today_word_single_digit_day,yesterday_word_single_digit_day]

## Headers is used because a User-Agent was required by the website
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.46'}
link = "https://www.dhs.gov/news-releases"

##** Error Handling for bad URL
try:
    page = requests.get(link, headers=headers)
    page.raise_for_status()
except:
    print('URL Broken')
    obj_list = [{'type':'Government','source':'Homeland Dept', 'title': 'Link Broken', 'link': '', 'Notes': '', 'date': ''}]
    homeland_df = pd.DataFrame(obj_list)
    
## Parse the webpage
page = requests.get(link, headers=headers)
soup = BeautifulSoup(page.content, 'lxml')

## Actual HTML pull
object_list = []

for item in soup.find_all(class_='usa-collection__item'):

    if item.find('time').attrs['datetime'][:-15] in date_list:
        title = item.find('a').get_text()
        ilink = "https://www.dhs.gov" + item.find('a').get('href')
        idate = item.find('time').attrs['datetime'][:-15]
        obj_data = {'type':'Government','source':'Homeland Dept', 'title': title, 'link': ilink, 'Notes': '', 'date': idate}
        object_list.append(obj_data)
    
if len(object_list) == 0:
    item = soup.find(class_='usa-collection__item')
    title = item.find('a').get_text()
    ilink = "https://www.dhs.gov" + item.find('a').get('href')
    idate = item.find('time').attrs['datetime'][:-15]
    obj_data = {'type':'Government','source':'Homeland Dept', 'title': title, 'link': ilink, 'Notes': 'Query Working, No New Posts', 'date': idate}
    object_list.append(obj_data)

## Final dataframe is defined
homeland_df = pd.DataFrame(object_list)

##** Error Handling for empty result
if len(homeland_df) == 0:
    print('No Result')
    obj_list = [{'type':'Government','source':'Homeland Dept', 'title': 'Data List Empty', 'link': '', 'Notes': '', 'date': ''}]
    homeland_df = pd.DataFrame(obj_list)

print(homeland_df)

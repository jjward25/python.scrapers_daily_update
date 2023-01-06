from bs4 import BeautifulSoup  ## BeautifulSoup is a web parsing package to help pull specific HTML components
import urllib.request  ## to get a access to a URL and its content
import pandas as pd 
from datetime import date, timedelta
import requests 

## Date List created with string values for the last 4 days to only pull opinions from that range.  
## General templates to pull from, not all are always used.
today = date.today()
yesterday = date.today() - timedelta(1)
today_word = today.strftime("%B %d, %Y")
today_word_single_digit_day = today.strftime("%B %d, %Y").replace(" 0", " ")
yesterday_word = yesterday.strftime("%B %d, %Y")
yesterday_word_single_digit_day = yesterday.strftime("%B %d, %Y").replace(" 0", " ")
today_new = today.strftime("%m/%d/%Y")
yesterday_new = yesterday.strftime("%m/%d/%Y")
date_list = [today_new,yesterday_new,today_word,yesterday_word,today_word_single_digit_day,yesterday_word_single_digit_day]
#print(date_list)

## Headers is used because a User-Agent was required by the website
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.46'}
link = "https://www.supremecourt.gov/opinions/slipopinion/22"

    ##** Error Handling for bad URL
try:
    page = requests.get(link, headers=headers)
    page.raise_for_status()
except:
    print('URL Broken')
    obj_list = [{'type':'Government','source':'Supreme Court', 'title': 'Link Broken', 'link': '', 'Notes': '', 'date': ''}]
    supreme_court_df = pd.DataFrame(obj_list)

page = requests.get(link, headers=headers)
soup = BeautifulSoup(page.content, 'lxml')

## Actual HTML pull
object_list = []

for item in soup.find_all('tr')[2:10]:
    #print(item.find_all('td')[1].get_text())
    if item.find_all('td')[1].get_text() in date_list:
        title = item.find_all('td')[1].get_text()
        ilink = item.find('a').get('href')
        #notes = item.find(class_='casedetail').get_text().strip('\n')
        idate = item.find_all('td')[1].get_text()
        obj_data = {'type':'Government','source':'Supreme Court', 'title': title, 'link': ilink, 'Notes': 'notes', 'date': idate}
        object_list.append(obj_data)

if len(object_list) == 0:
    obj_data = {'type':'Government','source':'Supreme Court', 'title': 'title', 'link': 'ilink', 'Notes': 'No New Cases', 'date': 'idate'}
    object_list.append(obj_data)

## Final dataframe is defined
supreme_court_df = pd.DataFrame(object_list)

##** Error Handling for empty result
if len(supreme_court_df) == 0:
    print('No Result')
    obj_list = [{'type':'Government','source':'Supreme Court', 'title': 'Data List Empty', 'link': '', 'Notes': '', 'date': ''}]
    supreme_court_df = pd.DataFrame(obj_list)
## Final Return Statement
print(supreme_court_df)

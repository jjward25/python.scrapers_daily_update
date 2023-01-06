from bs4 import BeautifulSoup  ## BeautifulSoup is a web parsing package to help pull specific HTML components
import urllib.request  ## to get a access to a URL and its content
import pandas as pd 
from datetime import date, timedelta, datetime
import requests 

## Date List created with string values for the last 4 days to only pull opinions from that range.  
## General templates to pull from, not all are always used.
today = date.today()
yesterday = date.today() - timedelta(1)
two_ago = date.today() - timedelta(2)
today_word = today.strftime("%B %d, %Y")
today_word_single_digit_day = today.strftime("%B %d, %Y").replace(" 0", " ")
yesterday_word = yesterday.strftime("%B %d, %Y")
yesterday_word_single_digit_day = yesterday.strftime("%B %d, %Y").replace(" 0", " ")
two_ago_word = two_ago.strftime("%B %d, %Y")
two_ago_word_single_digit_day = two_ago.strftime("%B %d, %Y").replace(" 0", " ")
date_list = [today_word,yesterday_word,two_ago_word,today_word_single_digit_day,yesterday_word_single_digit_day,two_ago_word_single_digit_day]

## Headers is used because a User-Agent was required by the website
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.46'}
link = "https://www.justice.gov/news"

##** Error Handling for bad URL
try:
    page = requests.get(link, headers=headers)
    page.raise_for_status()
except:
    print('URL Broken')
    obj_list = [{'type':'Government','source':'Justice Dept', 'title': 'Link Broken', 'link': '', 'Notes': '', 'date': ''}]
    justice_df = pd.DataFrame(obj_list)
    
## Parse the webpage
page = requests.get(link, headers=headers)
soup = BeautifulSoup(page.content, 'lxml')

## Actual HTML pull
object_list = []
stop_name = soup.find_all('h3')[1].find('span').get_text()
#print("stopname: " + stop_name)

content = soup.find_all(class_='view-content')[0]

for item in content:
    if (stop_name in str(item)):
        break
    if (item.find('a') == -1):
        continue
    if (type(item.find('a')) == type(None)):
        continue
    else:
        #print("result")
        #print(item)
        title = item.find('a').get_text()
        ilink = "https://www.justice.gov" + item.find('a').get('href')
        obj_data = {'type':'Government','source':'Justice Dept', 'title': title, 'link': ilink, 'Notes': 'notes', 'date': 'idate'}
        object_list.append(obj_data)

    
        
## Final dataframe is defined with duplicates removed
df = pd.DataFrame(object_list)
justice_df = df.drop_duplicates()

##** Error Handling for empty result
if len(justice_df) == 0:
    print('No Result')
    obj_list = [{'type':'Government','source':'Justice Dept', 'title': 'Data List Empty', 'link': '', 'Notes': '', 'date': ''}]
    justice_df = pd.DataFrame(obj_list)
## Final Return Statement
print(justice_df)


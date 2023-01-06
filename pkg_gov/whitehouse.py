from bs4 import BeautifulSoup  ## BeautifulSoup is a web parsing package to help pull specific HTML components
import urllib.request  ## to get a access to a URL and its content
import pandas as pd 
from datetime import date, timedelta
import requests 


## Date List created with string values for the last 4 days to only pull opinions from that range.  
## General templates to pull from, not all are always used.
today=date.today()
yesterday= date.today() - timedelta(1)
today_yyyymmdd = today.strftime("%Y/%m/%d")
yesterday_yyyymmdd = yesterday.strftime("%Y/%m/%d")
two_ago = date.today() - timedelta(2)
today_word = today.strftime("%B %d, %Y")
today_word_single_digit_day = today.strftime("%B %d, %Y").replace(" 0", " ")
yesterday_word = yesterday.strftime("%B %d, %Y")
yesterday_word_single_digit_day = yesterday.strftime("%B %d, %Y").replace(" 0", " ")
two_ago_word = two_ago.strftime("%B %d, %Y")
two_ago_word_single_digit_day = two_ago.strftime("%B %d, %Y").replace(" 0", " ")
date_list = [today_word,yesterday_word,two_ago_word,today_word_single_digit_day,yesterday_word_single_digit_day,two_ago_word_single_digit_day]

## HTML details and beautiful soup's initial pull of all HTML elements
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.46'}
link = "https://www.whitehouse.gov/briefing-room/"

    ##** Error Handling for bad URL
try:
    page = requests.get(link, headers=headers)
    page.raise_for_status()
except:
    print('URL Broken')
    obj_list = [{'type':'Government','source':'White House', 'title': 'Link Broken', 'link': '', 'Notes': '', 'date': ''}]
    white_house_df = pd.DataFrame(obj_list)

page = urllib.request.urlopen(link)
soup = BeautifulSoup(page, 'html.parser')
#print(soup)

## Final data pull
object_list = []

for item in soup.find_all(class_="news-item"):
    if item.find('time').get_text() in date_list:
        title = item.find(class_='news-item__title').get_text().partition('\t\t\t\t')[2]
        ilink = item.find(class_='news-item__title').get('href')
        #notes = item.find(class_='field--type-text-with-summary').get_text()
        idate = item.find('time').get_text()
        obj_data = {'type':'Government','source':'White House', 'title': title, 'link': ilink, 'Notes': 'notes', 'date': idate}
        object_list.append(obj_data)

if len(object_list) == 0:
    item = soup.find(class_="news-item")
    title = item.find(class_='news-item__title').get_text().partition('\t\t\t\t')[2]
    ilink = item.find(class_='news-item__title').get('href')
    #notes = item.find(class_='field--type-text-with-summary').get_text()
    idate = item.find('time').get_text()
    obj_data = {'type':'Government','source':'White House', 'title': title, 'link': ilink, 'Notes': 'Query Working, No New Posts', 'date': idate}
    object_list.append(obj_data)

## Final dataframe is defined
white_house_df = pd.DataFrame(object_list)

##** Error Handling for empty result
if len(white_house_df) == 0:
    print('No Result')
    obj_list = [{'type':'Government','source':'White House', 'title': 'Data List Empty', 'link': '', 'Notes': '', 'date': ''}]
    white_house_df = pd.DataFrame(obj_list)
## Final Return Statement
print(white_house_df)
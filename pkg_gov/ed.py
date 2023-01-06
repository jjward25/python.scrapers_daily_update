from bs4 import BeautifulSoup  ## BeautifulSoup is a web parsing package to help pull specific HTML components
import pandas as pd 
from datetime import date, timedelta, datetime
import requests 

## Date List created with string values for the last 4 days to only pull opinions from that range.  
## General templates to pull from, not all are always used.
today = date.today()
yesterday = date.today() - timedelta(1)
today_word = today.strftime("%B %d, %Y")
today_word_single_digit_day = today.strftime("%B %d, %Y").replace(" 0", " ")
yesterday_word = yesterday.strftime("%B %d, %Y")
yesterday_word_single_digit_day = yesterday.strftime("%B %d, %Y").replace(" 0", " ")
date_list = [today_word,yesterday_word,today_word_single_digit_day,yesterday_word_single_digit_day]

## Headers is used because a User-Agent was required by the website
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.46'}
link = "https://www.ed.gov/news/press-releases"

##** Error Handling for bad URL
try:
    page = requests.get(link, headers=headers)
    page.raise_for_status()
except:
    print('URL Broken')
    obj_list = [{'type':'Government','source':'Ed Dept', 'title': 'Link Broken', 'link': '', 'Notes': '', 'date': ''}]
    education_df = pd.DataFrame(obj_list)
    
## Parse the webpage
page = requests.get(link, headers=headers)
soup = BeautifulSoup(page.content, 'lxml')

## Actual HTML pull
object_list = []
for item in soup.find_all(class_='views-row'):
    ## Transforms the time tag from a string to date format, then into the right date format and checks to see if it's in the date_list object
    if datetime.strptime(item.find_all('span')[0].get_text(), '%B %d, %Y').strftime("%B %d, %Y") in date_list:
        title = item.find_all(class_='views-field')[1].get_text()
        ilink = item.find('a').get('href')
        notes = item.find(class_="views-field-body").get_text()
        idate = item.find_all('span')[0].get_text()
        obj_data = {'type':'Government','source':'Ed Dept', 'title': title, 'link': ilink, 'Notes': notes, 'date': idate}
        object_list.append(obj_data)

if len(object_list) == 0:
    item = soup.find(class_='views-row')
    title = item.find_all(class_='views-field')[1].get_text()
    ilink = item.find('a').get('href')
    notes = item.find(class_="views-field-body").get_text()
    idate = item.find_all('span')[0].get_text()
    obj_data = {'type':'Government','source':'Ed Dept', 'title': title, 'link': ilink, 'Notes': 'Query Working, No New Posts', 'date': idate}
    object_list.append(obj_data)

## Final dataframe is defined
education_df = pd.DataFrame(object_list)

##** Error Handling for empty result
if len(education_df) == 0:
    print('No Result')
    obj_list = [{'type':'Government','source':'Ed Dept', 'title': 'Data List Empty', 'link': '', 'Notes': '', 'date': ''}]
    education_df = pd.DataFrame(obj_list)

print(education_df)
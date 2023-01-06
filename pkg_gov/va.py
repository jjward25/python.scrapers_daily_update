from bs4 import BeautifulSoup  ## BeautifulSoup is a web parsing package to help pull specific HTML components
import pandas as pd 
from datetime import date, timedelta, datetime
import requests 

## Date List created with string values for the last 4 days to only pull opinions from that range.  
## General templates to pull from, not all are always used.
today = date.today()
today_hyphens = today.strftime("%Y-%m-%d")
#today_word = today.strftime("%B %d, %Y")
today_word = today.strftime("%B %dth, %Y").replace('2023','9999').replace("0", "").replace('9999','2023')
today_word_single_digit_day = today.strftime("%B %d, %Y").replace(" 0", " ")

yesterday = date.today() - timedelta(1)
yesterday_hypens = yesterday.strftime("%Y-%m-%d")
#yesterday_word = yesterday.strftime("%B %d, %Y")
yesterday_word = yesterday.strftime("%B %dth, %Y").replace('2023','9999').replace("0", "").replace('9999','2023')
yesterday_word_single_digit_day = yesterday.strftime("%B %d, %Y").replace(" 0", " ")

two_ago = date.today() - timedelta(2)
two_ago_hypens = two_ago.strftime("%Y-%m-%d")
#two_ago_word = two_ago.strftime("%B %d, %Y")
two_ago_word = two_ago.strftime("%B %dth, %Y").replace('2023','9999').replace("0", "").replace('9999','2023')
two_ago_word_single_digit_day = two_ago.strftime("%B %d, %Y").replace(" 0", " ")

date_list = [today_hyphens,yesterday_hypens,two_ago_hypens,today_word,yesterday_word,two_ago_word,today_word_single_digit_day,yesterday_word_single_digit_day,two_ago_word_single_digit_day]
#print(date_list)
year = today.strftime("%Y")
month = today.strftime("%m")
# print(date_list)

## Headers is used because a User-Agent was required by the website
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.46'}
link = "https://blogs.va.gov/VAntage/date/"+year+"/"+month+"/"

##** Error Handling for bad URL
try:
    page = requests.get(link, headers=headers)
    page.raise_for_status()
except:
    print('URL Broken')
    obj_list = [{'type':'Government','source':'VA Dept', 'title': 'Link Broken', 'link': '', 'Notes': '', 'date': ''}]
    va_df = pd.DataFrame(obj_list)
    
## Parse the webpage
page = requests.get(link, headers=headers)
soup = BeautifulSoup(page.content, 'lxml')

## Actual HTML pull
object_list = []
for item in soup.find_all('article'):
    title = item.find('h2').find('a').get_text()
    ilink = item.find('a').get('href')
    notes = item.find()
    idate = item.find(class_='fusion-single-line-meta').find_all('span')[3].get_text()
    if idate in date_list:
        obj_data = {'type':'Government','source':'VA Dept', 'title': title, 'link': ilink, 'Notes': 'notes', 'date': idate}
        object_list.append(obj_data)

if len(object_list) == 0:
    item = soup.find('article')
    title = item.find('h2').find('a').get_text()
    ilink = item.find('a').get('href')
    notes = item.find()
    idate = item.find(class_='fusion-single-line-meta').find_all('span')[3].get_text()
    obj_data = {'type':'Government','source':'VA Dept', 'title': title, 'link': ilink, 'Notes': 'Query Working, No New Posts', 'date': idate}
    object_list.append(obj_data)

## Final dataframe is defined
va_df = pd.DataFrame(object_list)

##** Error Handling for empty result
if len(va_df) == 0:
    print('No Result')
    obj_list = [{'type':'Government','source':'VA Dept', 'title': 'Data List Empty', 'link': '', 'Notes': '', 'date': ''}]
    va_df = pd.DataFrame(obj_list)
## Final Return Statement
print(va_df)

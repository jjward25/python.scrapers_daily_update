from bs4 import BeautifulSoup  ## BeautifulSoup is a web parsing package to help pull specific HTML components
import urllib.request  ## to get a access to a URL and its content
import pandas as pd 
from datetime import date, timedelta, datetime
import requests 

## Date List created with string values for the last 4 days to only pull opinions from that range.
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

## Headers is used because a User-Agemt was required by the website
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.46'}
link = ""
page = requests.get(link, headers=headers)
soup = BeautifulSoup(page.content, 'lxml')

## Actual HTML pull
object_list = []
for item in soup.find_all(class_=''):

    #if item.find('span').get_text() in date_list:  ## Checks if the date is in the last 3 days

    title = item.find()
    ilink = item.find()
    notes = item.find()
    idate = item.find()

    obj_data = {'source':'', 'title': '', 'link': '', 'Notes': '', 'date': ''}
    object_list.append(obj_data)

## Final dataframe is defined
_dept_df = pd.DataFrame(object_list)
print(_dept_df)
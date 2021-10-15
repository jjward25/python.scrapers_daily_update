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
yesterday_word = yesterday.strftime("%B %d, %Y")
two_ago_word = two_ago.strftime("%B %d, %Y")
#print(today_word)
#print(yesterday_word)
#print(two_ago_word)
date_list = [today_word,yesterday_word,two_ago_word]

## Headers is used because a User-Agemt was required by the website
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.46'}
link = "https://www.justice.gov/"
page = requests.get(link, headers=headers)
soup = BeautifulSoup(page.content, 'lxml')

## Actual HTML pull
object_list = []

##Pulls contents from different primary elements and uses a try and except format to print only relevant articles
for item in range(10):
    try:
        if datetime.strptime(soup.find_all(class_='views-row')[item].find(class_='date-display-single').get_text(), '%A, %B %d, %Y').strftime("%B %d, %Y") in date_list:

            idate = soup.find_all(class_='views-row')[item].find(class_='date-display-single').get_text()
            title = soup.find_all(class_='views-row')[item].find('a').get_text()
            ilink = "https://www.justice.gov" + soup.find_all(class_='views-row')[item].find('a').get('href')

            obj_data = {'source':'Justice Dept', 'title': title, 'link': ilink, 'Notes': 'notes', 'date': idate}
            object_list.append(obj_data)
        
    except: 
        pass

## Final dataframe is defined with duplicates removed
df = pd.DataFrame(object_list)
justice_dept_df = df.drop_duplicates()
print(justice_dept_df)
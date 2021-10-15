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
today_link = today.strftime("%Y/%m/%d/")
#print(today_word)
#print(yesterday_word)
#print(two_ago_word)
date_list = [today_word,yesterday_word,two_ago_word]

## Headers is used because a User-Agemt was required by the website
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.46'}
link = "https://www.politico.com/search?adv=true&userInitiated=true&s=newest&q=&pv=&c=0000016c-7218-df3f-a1fe-779a301e0006&r=&start=&start_submit=&end=&end_submit="
page = requests.get(link, headers=headers)
soup = BeautifulSoup(page.content, 'lxml')

## Actual HTML pull
object_list = []
for item in soup.find_all(class_='summary'):
    #if item.find('span').get_text() in date_list:
    title = item.find('a').get_text()
    ilink = item.find('a').get('href')  
    notes = item.find(class_='tease').get_text().lstrip('\n')
    idate = item.find('time').get_text()

    obj_data = {'source':'Politico', 'title': title, 'link': ilink, 'Notes': notes, 'date': idate}
    object_list.append(obj_data)

## Final dataframe is defined
politico_df = pd.DataFrame(object_list).head(8)
print(politico_df)
from bs4 import BeautifulSoup  ## BeautifulSoup is a web parsing package to help pull specific HTML components
import urllib.request  ## to get a access to a URL and its content
import pandas as pd 
from datetime import date, timedelta, datetime
import requests 

## Headers is used because a User-Agemt was required by the website
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.46'}
link = "https://www.reuters.com/legal/"
page = requests.get(link, headers=headers)
soup = BeautifulSoup(page.content, 'lxml')

test = soup.find_all(class_='story-card')[0]
print(test)

## Actual HTML pull
object_list = []
for item in soup.find_all(class_='MediaStoryCard__no_meta___3iQjxw StaticMediaMaximizer__card___2_CdUh'):
    #if item.find('span').get_text() in date_list:
    title = item.get_text()
    ilink = "https://www.reuters.com" + str(item.get('href'))
    #notes = item.find(class_='summary f-serif ls-0').get_text()
    #idate = item.find(class_='publication-date').get_text()

    obj_data = {'source':'Reuters Legal', 'title': title, 'link': ilink, 'Notes': 'notes', 'date': 'idate'}
    object_list.append(obj_data)

## Final dataframe is defined
reuters_legal_df = pd.DataFrame(object_list).head(8)
print(reuters_legal_df)
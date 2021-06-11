from bs4 import BeautifulSoup  ## BeautifulSoup is a web parsing package to help pull specific HTML components
import urllib.request  ## to get a access to a URL and its content
import pandas as pd 
from datetime import date, timedelta, datetime
import requests 

## Headers is used because a User-Agemt was required by the website
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.46'}
link = "https://home.treasury.gov/news/press-releases"
page = requests.get(link, headers=headers)
soup = BeautifulSoup(page.content, 'lxml')

## Actual HTML pull
object_list = []

##just pulls the last 4 articles, doesn't limit by date
for item in range(4):

    idate = soup.find_all(class_='date-format')[item].find('time').get_text()
    title = soup.find_all(class_='featured-stories__headline')[item].find('a').get_text()
    ilink = soup.find_all(class_='featured-stories__headline')[item].find('a').get('href')

    obj_data = {'source':'Treasury Dept', 'title': title, 'link': ilink, 'Notes': 'notes', 'date': idate}
    object_list.append(obj_data)

## Final dataframe is defined with duplicates removed
df = pd.DataFrame(object_list)
treasury_dept_df = df.drop_duplicates()
print(treasury_dept_df)
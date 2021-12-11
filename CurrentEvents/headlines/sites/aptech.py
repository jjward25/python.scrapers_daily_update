from bs4 import BeautifulSoup  ## BeautifulSoup is a web parsing package to help pull specific HTML components
import urllib.request  ## to get a access to a URL and its content
import pandas as pd 
from datetime import date, timedelta, datetime
import requests 

## Headers is used because a User-Agemt was required by the website
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.46'}
link = "https://apnews.com/hub/technology?utm_source=apnewsnav&utm_medium=navigation"
page = requests.get(link, headers=headers)
soup = BeautifulSoup(page.content, 'lxml')

test = soup.find_all(class_='CardHeadline')[0]
#print(test)

print(soup.find_all(class_='CardHeadline')[0])


## Actual HTML pull
object_list = []
for item in soup.find_all(class_='CardHeadline'):
    
    title = item.get_text()
    ilink = "https://www.apnews.com" + str(item.find(class_='Component-headline-0-2-106').get('href'))
    #notes = item.find(class_='summary f-serif ls-0').get_text()
    #idate = item.find(class_='publication-date').get_text()

    obj_data = {'source':'AP Tech', 'title': title, 'link': ilink, 'Notes': 'notes', 'date': 'idate'}
    object_list.append(obj_data)

## Final dataframe is defined
aptech_df = pd.DataFrame(object_list).head(8)
print(aptech_df)
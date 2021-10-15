from bs4 import BeautifulSoup  ## BeautifulSoup is a web parsing package to help pull specific HTML components
import urllib.request  ## to get a access to a URL and its content
import pandas as pd 
from datetime import date, timedelta, datetime
import requests 

## Date List created with string values for the last 3 days to only pull articles from that range.
today = date.today()
#yesterday = date.today() - timedelta(1)
#two_ago = date.today() - timedelta(2)
#today_word = today.strftime("%B %d, %Y")
#yesterday_word = yesterday.strftime("%B %d, %Y")
#two_ago_word = two_ago.strftime("%B %d, %Y")
#today_link = today.strftime("%Y/%m/%d/")
year = today.strftime("%Y")
month = today.strftime("%m")
#print(today_word)
#print(yesterday_word)
#print(two_ago_word)
#date_list = [today_word,yesterday_word,two_ago_word]

## Headers is used because a User-Agemt was required by the website
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.46'}
link = "https://blogs.va.gov/VAntage/date/"+year+"/"+month+"/"
page = requests.get(link, headers=headers)
soup = BeautifulSoup(page.content, 'lxml')
print(soup)
## Actual HTML pull
object_list = []
for item in soup.find_all('article'):

    #if item.find('span').get_text() in date_list:

    title = item.find('h2').find('a').get_text()
    ilink = item.find('a').get('href')
    notes = item.find()
    idate = item.find(class_='updated rich-snippet-hidden').get_text()
    
    

    obj_data = {'source':'VA Dept', 'title': title, 'link': ilink, 'Notes': 'notes', 'date': idate}
    object_list.append(obj_data)

## Final dataframe is defined
va_dept_df = pd.DataFrame(object_list)
print(va_dept_df)
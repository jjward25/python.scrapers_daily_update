from bs4 import BeautifulSoup  ## BeautifulSoup is a web parsing package to help pull specific HTML components
import urllib.request  ## to get a access to a URL and its content
import pandas as pd 
from datetime import date, timedelta
import requests 

today = date.today()
yesterday = date.today() - timedelta(1)
two_ago = date.today() - timedelta(2)
three_ago = date.today() - timedelta(3)
today_word = today.strftime("%B %d, %Y")
yesterday_word = yesterday.strftime("%B %d, %Y")
two_ago_word = two_ago.strftime("%B %d, %Y")
three_ago_word = three_ago.strftime("%B %d, %Y")
#print(today_word)
#print(yesterday_word)
#print(two_ago_word)
#print(three_ago_word)
date_list = []
date_list = date_list.append(today_word)
date_list = date_list.append(yesterday_word)
date_list = date_list.append(two_ago_word)
date_list = date_list.append(three_ago_word)


headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.46'}
link = "https://www.supremecourt.gov/"
page = requests.get(link, headers=headers)
soup = BeautifulSoup(page.content, 'lxml')

object_list = []
for item in soup.find_all(id='opinionsbyday'):

    if item.find('span').get_text() in date_list:

        title = item.find(class_='casenamerow').get_text().strip('\n')
        ilink = item.find('a').get('href')
        notes = item.find(class_='casedetail').get_text().strip('\n')
        idate = item.find('span').get_text()

        obj_data = {'source':'Supreme Court', 'title': title, 'link': ilink, 'Notes': notes, 'date': idate}
        object_list.append(obj_data)
        
supreme_court_df = pd.DataFrame(object_list)
print(supreme_court_df)
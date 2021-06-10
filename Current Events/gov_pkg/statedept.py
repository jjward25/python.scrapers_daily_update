from bs4 import BeautifulSoup  ## BeautifulSoup is a web parsing package to help pull specific HTML components
import urllib.request  ## to get a access to a URL and its content
import pandas as pd 
from datetime import date, timedelta

today=date.today()
yesterday= date.today() - timedelta(1)
today_yyyymmdd = today.strftime("%Y/%m/%d")
yesterday_yyyymmdd = yesterday.strftime("%Y/%m/%d")
#print(today_yyyymmdd)
#print(yesterday_yyyymmdd)

link = "https://www.state.gov/press-releases/"
page = urllib.request.urlopen(link)
soup = BeautifulSoup(page, 'html.parser')
#print(soup)

object_list = []
for item in soup.find_all():
    
    if today_yyyymmdd in item.get('href'):
        title = item.contents[0].lstrip('\n\t\t\t\t').lstrip() + item.find("span").get_text()
        #print(title)
        ilink=item.get('href')
        #print(link)
        obj_data = {'source':'White House', 'title': title, 'link': ilink, 'Notes':'', 'date':today}
        object_list.append(obj_data)

    if yesterday_yyyymmdd in item.get('href'):
        title = item.contents[0].lstrip('\n\t\t\t\t').lstrip() + item.find("span").get_text()
        #print(title)
        ilink=item.get('href')
        #print(link)
        obj_data = {'source':'White House', 'title': title, 'link': ilink, 'Notes':'','date':yesterday}
        object_list.append(obj_data)
        
#print(object_list)
state_dept_df = pd.DataFrame(object_list)
print(state_dept_df)
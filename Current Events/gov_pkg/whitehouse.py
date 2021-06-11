from bs4 import BeautifulSoup  ## BeautifulSoup is a web parsing package to help pull specific HTML components
import urllib.request  ## to get a access to a URL and its content
import pandas as pd 
from datetime import date, timedelta

## Date values are created to limit the final result
today=date.today()
yesterday= date.today() - timedelta(1)
today_yyyymmdd = today.strftime("%Y/%m/%d")
yesterday_yyyymmdd = yesterday.strftime("%Y/%m/%d")
#print(today_yyyymmdd)
#print(yesterday_yyyymmdd)

## HTML details and beautiful soup's initial pull of all HTML elements
link = "https://www.whitehouse.gov/briefing-room/"
page = urllib.request.urlopen(link)
soup = BeautifulSoup(page, 'html.parser')
#print(soup)


## Final data pull
object_list = []
for item in soup.find_all(class_="news-item__title"):
    
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
        
## Final dataframe is defined
white_house_df = pd.DataFrame(object_list)
print(white_house_df)
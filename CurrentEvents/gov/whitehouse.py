from bs4 import BeautifulSoup  ## BeautifulSoup is a web parsing package to help pull specific HTML components
import urllib.request  ## to get a access to a URL and its content
import pandas as pd 
from datetime import date, timedelta
import requests 


def whitehouse_scrape():
    ## Date List created with string values for the last 4 days to only pull opinions from that range.  
    ## General templates to pull from, not all are always used.
    today=date.today()
    yesterday= date.today() - timedelta(1)
    today_yyyymmdd = today.strftime("%Y/%m/%d")
    yesterday_yyyymmdd = yesterday.strftime("%Y/%m/%d")

    ## HTML details and beautiful soup's initial pull of all HTML elements
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.46'}
    link = "https://www.whitehouse.gov/briefing-room/"

     ##** Error Handling for bad URL
    try:
        page = requests.get(link, headers=headers)
        page.raise_for_status()
    except:
        print('URL Broken')
        obj_list = [{'type':'Government','source':'White House', 'title': 'Link Broken', 'link': '', 'Notes': '', 'date': ''}]
        white_house_df = pd.DataFrame(obj_list)
        return white_house_df

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
            obj_data = {'type':'Government','source':'White House', 'title': title, 'link': ilink, 'Notes':'', 'date':today}
            object_list.append(obj_data)

        if yesterday_yyyymmdd in item.get('href'):
            title = item.contents[0].lstrip('\n\t\t\t\t').lstrip() + item.find("span").get_text()
            #print(title)
            ilink=item.get('href')
            #print(link)
            obj_data = {'type':'Government','source':'White House', 'title': title, 'link': ilink, 'Notes':'','date':yesterday}
            object_list.append(obj_data)
            
    ## Final dataframe is defined
    white_house_df = pd.DataFrame(object_list)

    ##** Error Handling for empty result
    if len(white_house_df) == 0:
        print('URL Broken')
        obj_list = [{'type':'Government','source':'White House', 'title': 'Data List Empty', 'link': '', 'Notes': '', 'date': ''}]
        white_house_df = pd.DataFrame(obj_list)
        return white_house_df
    ## Final Return Statement
    return white_house_df


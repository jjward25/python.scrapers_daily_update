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
date_list = [today_word,yesterday_word,two_ago_word]

def cfr_scrape():
    ## Date List created with string values for the last 4 days to only pull opinions from that range.  
    ## General templates to pull from, not all are always used.
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.46'}
    link = "https://www.foreignaffairs.com/search/"

    ##** Error Handling for bad URL
    try:
        page = requests.get(link, headers=headers)
        page.raise_for_status()
    except:
        print('URL Broken')
        obj_list = [{'type':'OpEds','source':'CFR', 'title': 'Link Broken', 'link': '', 'Notes': '', 'date': ''}]
        cfr_df = pd.DataFrame(obj_list)
        return cfr_df
        
    ## Parse the webpage
    page = requests.get(link, headers=headers)
    soup = BeautifulSoup(page.content, 'lxml')

    test = soup.find_all('article')
    #print(test)
    print(soup.find_all('article'))
    ## Actual HTML pull
    object_list = []
    for item in soup.find_all('article'):
        #print(item)
        #if item.find('span').get_text() in date_list:
        title = item.find('a').get_text()
        ilink = item.find('a').get('href')
        #notes = item.find(class_='summary f-serif ls-0').get_text()
        #idate = item.find(class_='publication-date').get_text()

        obj_data = {'type':'OpEds','source':'CFR', 'title': title, 'link': ilink, 'Notes': 'notes', 'date': 'idate'}
        object_list.append(obj_data)

    ## Final dataframe is defined
    cfr_df = pd.DataFrame(object_list).head(8)

    ##** Error Handling for empty result
    if len(cfr_df) == 0:
        print('No Result')
        obj_list = [{'type':'OpEds','source':'CFR', 'title': 'Data List Empty', 'link': '', 'Notes': '', 'date': ''}]
        cfr_df = pd.DataFrame(obj_list)
        return cfr_df
    ## Final Return Statement
    print(cfr_df)
    return cfr_df

cfr_scrape()
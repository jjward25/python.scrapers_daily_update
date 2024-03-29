from bs4 import BeautifulSoup  ## BeautifulSoup is a web parsing package to help pull specific HTML components
import urllib.request  ## to get a access to a URL and its content
import pandas as pd 
from datetime import date, timedelta, datetime
import requests 

def nationalreview_scrape():
    ## Date List created with string values for the last 4 days to only pull opinions from that range.  
    ## General templates to pull from, not all are always used.
    today = date.today()
    yesterday = date.today() - timedelta(1)
    two_ago = date.today() - timedelta(2)
    today_word = today.strftime("%B %d, %Y")
    yesterday_word = yesterday.strftime("%B %d, %Y")
    two_ago_word = two_ago.strftime("%B %d, %Y")
    today_link = today.strftime("%Y/%m/%d/")
    date_list = [today_word,yesterday_word,two_ago_word]

    ## Headers is used because a User-Agemt was required by the website
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.46'}
    link = "https://www.nationalreview.com/latest/"

    ##** Error Handling for bad URL
    try:
        page = requests.get(link, headers=headers)
        page.raise_for_status()
    except:
        print('URL Broken')
        obj_list = [{'type':'OpEds','source':'National Review', 'title': 'Link Broken', 'link': '', 'Notes': '', 'date': ''}]
        national_review_df = pd.DataFrame(obj_list)
        return national_review_df
        
    ## Parse the webpage
    page = requests.get(link, headers=headers)
    soup = BeautifulSoup(page.content, 'lxml')

    ## Actual HTML pull
    object_list = []
    for item in soup.find_all(class_='post-list-article__text'):
        #if item.find('span').get_text() in date_list:
        title = item.find(class_='post-list-article__title').find('a').get_text()
        ilink = item.find(class_='post-list-article__title').find('a').get('href')
        notes = item.find(class_='post-list-article__entry')
        idate = item.find()

        obj_data = {'type':'OpEds','source':'National Review', 'title': title, 'link': ilink, 'Notes': notes, 'date': ''}
        object_list.append(obj_data)

    ## Final dataframe is defined
    national_review_df = pd.DataFrame(object_list).head(6)

        ##** Error Handling for empty result
    if len(national_review_df) == 0:
        print('No Result')
        obj_list = [{'type':'OpEds','source':'National Review', 'title': 'Data List Empty', 'link': '', 'Notes': '', 'date': ''}]
        national_review_df = pd.DataFrame(obj_list)
        return national_review_df
    ## Final Return Statement
    print(national_review_df)
    return national_review_df

nationalreview_scrape()
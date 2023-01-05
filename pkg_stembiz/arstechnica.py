from bs4 import BeautifulSoup  ## BeautifulSoup is a web parsing package to help pull specific HTML components
import urllib.request  ## to get a access to a URL and its content
import pandas as pd 
from datetime import date, timedelta, datetime
import requests 

def ars_scrape():
    ## Date List created with string values for the last 4 days to only pull opinions from that range.  
    ## General templates to pull from, not all are always used.
    today = date.today()
    yesterday = date.today() - timedelta(1)
    two_ago = date.today() - timedelta(2)
    today_word = today.strftime("%b %d, %Y").replace('2023','9999').replace("0", "").replace('9999','2023')
    yesterday_word = yesterday.strftime("%b %d, %Y").replace('2023','9999').replace("0", "").replace('9999','2023')
    two_ago_word = two_ago.strftime("%b %d, %Y").replace('2023','9999').replace("0", "").replace('9999','2023')
    today_link = today.strftime("%m/%d/%Y").replace('2023','9999').replace("0", "").replace('9999','2023')
    yesterday_link = yesterday.strftime("%m/%d/%Y").replace('2023','9999').replace("0", "").replace('9999','2023')
    two_ago_link = two_ago.strftime("%m/%d/%Y").replace('2023','9999').replace("0", "").replace('9999','2023')
    date_list = [today_word,yesterday_word,two_ago_word,today_link,yesterday_link,two_ago_link]
    print(date_list)

    ## Headers is used because a User-Agemt was required by the website
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.46'}
    link = "https://arstechnica.com/"

    ##** Error Handling for bad URL
    try:
        page = requests.get(link, headers=headers)
        page.raise_for_status()
    except:
        print('URL Broken')
        obj_list = [{'type':'Headline','source':'Ars Technica', 'title': 'Link Broken', 'link': '', 'Notes': '', 'date': ''}]
        ars_df = pd.DataFrame(obj_list)
        return ars_df
        
    ## Parse the webpage
    page = requests.get(link, headers=headers)
    soup = BeautifulSoup(page.content, 'lxml')

    ## Actual HTML pull
    object_list = []
    for item in soup.find_all('header')[0:10]:
        if item.find('time') is not None:
            # predefine the date value because depending on how many digits are in the day, there might be a trailing zero that needs to be removed
            postdate = item.find('time').get_text()[0:12]
            if postdate[-1] == " ":
                postdate = postdate[:11]
            else:
                postdate = postdate

            if postdate in date_list:
                #if item.find('span').get_text() in date_list:
                title = item.find('a').get_text()
                ilink = item.find('a').get('href')  
                #notes = item.find(class_='tease').get_text().lstrip('\n')
                idate = item.find('time').get_text().partition(',')[1]
                obj_data = {'type':'Headline','source':'Ars Technica', 'title': title, 'link': ilink, 'Notes': '', 'date': idate}
                object_list.append(obj_data)

    ## Final dataframe is defined
    ars_df = pd.DataFrame(object_list)

        ##** Error Handling for empty result
    if len(ars_df) == 0:
        print('No Results')
        obj_list = [{'type':'Headline','source':'Ars Technica', 'title': 'Data List Empty', 'link': '', 'Notes': '', 'date': ''}]
        ars_df = pd.DataFrame(obj_list)
        return ars_df
    ## Final Return Statement
    print(ars_df)
    return ars_df

ars_scrape()
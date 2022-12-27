from bs4 import BeautifulSoup  ## BeautifulSoup is a web parsing package to help pull specific HTML components
import urllib.request  ## to get a access to a URL and its content
import pandas as pd 
from datetime import date, timedelta, datetime
import requests 

def justice_scrape():
    ## Date List created with string values for the last 4 days to only pull opinions from that range.  
    ## General templates to pull from, not all are always used.
    today = date.today()
    yesterday = date.today() - timedelta(1)
    two_ago = date.today() - timedelta(2)
    today_word = today.strftime("%B %d, %Y")
    today_word_single_digit_day = today.strftime("%B %d, %Y").replace(" 0", " ")
    yesterday_word = yesterday.strftime("%B %d, %Y")
    yesterday_word_single_digit_day = yesterday.strftime("%B %d, %Y").replace(" 0", " ")
    two_ago_word = two_ago.strftime("%B %d, %Y")
    two_ago_word_single_digit_day = two_ago.strftime("%B %d, %Y").replace(" 0", " ")
    date_list = [today_word,yesterday_word,two_ago_word,today_word_single_digit_day,yesterday_word_single_digit_day,two_ago_word_single_digit_day]

    ## Headers is used because a User-Agent was required by the website
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.46'}
    link = "https://www.justice.gov/"

    ##** Error Handling for bad URL
    try:
        page = requests.get(link, headers=headers)
        page.raise_for_status()
    except:
        print('URL Broken')
        obj_list = [{'type':'Government','source':'Justice Dept', 'title': 'Link Broken', 'link': '', 'Notes': '', 'date': ''}]
        justice_dept_df = pd.DataFrame(obj_list)
        return justice_dept_df
        
    ## Parse the webpage
    page = requests.get(link, headers=headers)
    soup = BeautifulSoup(page.content, 'lxml')

    ## Actual HTML pull
    object_list = []

    ##Pulls contents from different primary elements and uses a try and except format to print only relevant articles
    for item in range(10):
        try:
            if datetime.strptime(soup.find_all(class_='views-row')[item].find(class_='date-display-single').get_text(), '%A, %B %d, %Y').strftime("%B %d, %Y") in date_list:

                idate = soup.find_all(class_='views-row')[item].find(class_='date-display-single').get_text()
                title = soup.find_all(class_='views-row')[item].find('a').get_text()
                ilink = "https://www.justice.gov" + soup.find_all(class_='views-row')[item].find('a').get('href')

                obj_data = {'type':'Government','source':'Justice Dept', 'title': title, 'link': ilink, 'Notes': 'notes', 'date': idate}
                object_list.append(obj_data)
            
        except: 
            pass

    ## Final dataframe is defined with duplicates removed
    df = pd.DataFrame(object_list)
    justice_dept_df = df.drop_duplicates()

    ##** Error Handling for empty result
    if len(justice_dept_df) == 0:
        print('No Result')
        obj_list = [{'type':'Government','source':'Justice Dept', 'title': 'Data List Empty', 'link': '', 'Notes': '', 'date': ''}]
        justice_dept_df = pd.DataFrame(obj_list)
        return justice_dept_df
    ## Final Return Statement
    print(justice_dept_df)
    return justice_dept_df

justice_scrape()
from bs4 import BeautifulSoup  ## BeautifulSoup is a web parsing package to help pull specific HTML components
import pandas as pd 
from datetime import date, timedelta, datetime
import requests 

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

def treasury_scrape():
    ## Headers is used because a User-Agemt was required by the website
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.46'}
    link = "https://home.treasury.gov/news/press-releases"
    page = requests.get(link, headers=headers)
    soup = BeautifulSoup(page.content, 'lxml')
    
    ## Actual HTML pull
    object_list = []
    ##just pulls the last 4 articles, doesn't limit by date
    for item in range(10):

        idate = soup.find_all(class_='date-format')[item].find('time').get_text()[:-15]
        title = soup.find_all(class_='featured-stories__headline')[item].find('a').get_text()
        ilink = "https://home.treasury.gov" + soup.find_all(class_='featured-stories__headline')[item].find('a').get('href')
        if idate in date_list:
            obj_data = {'type':'Government','source':'Treasury Dept', 'title': title, 'link': ilink, 'Notes': 'notes', 'date': idate}
            object_list.append(obj_data)

    if len(object_list) == 0:
        for item in range(1):
            idate = soup.find_all(class_='date-format')[item].find('time').get_text()
            title = soup.find_all(class_='featured-stories__headline')[item].find('a').get_text()
            ilink = "https://home.treasury.gov" + soup.find_all(class_='featured-stories__headline')[item].find('a').get('href')
            obj_data = {'type':'Government','source':'Treasury Dept', 'title': title, 'link': ilink, 'Notes': 'Query Working, No New Posts', 'date': idate}
            object_list.append(obj_data)
    
    ## Final dataframe is defined with duplicates removed
    df = pd.DataFrame(object_list)
    treasury_dept_df = df.drop_duplicates()
    print(treasury_dept_df)
    return treasury_dept_df

treasury_scrape()
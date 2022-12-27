from bs4 import BeautifulSoup  ## BeautifulSoup is a web parsing package to help pull specific HTML components
import pandas as pd 
from datetime import date, timedelta, datetime
import requests 

def agriculture_scrape():
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
    link = "https://www.usda.gov/media/press-releases"

    ##** Error Handling for bad URL
    try:
        page = requests.get(link, headers=headers)
        page.raise_for_status()
    except:
        print('URL Broken')
        obj_list = [{'type':'Government','source':'Agriculture Dept', 'title': 'Link Broken', 'link': '', 'Notes': '', 'date': ''}]
        agriculture_dept_df = pd.DataFrame(obj_list)
        return agriculture_dept_df
        
    ## Parse the webpage
    soup = BeautifulSoup(page.content, 'lxml')
    element = 'news-releases-item' ##!! define the html element to search for
    
    test = soup.find_all(class_=element)
    if len(test) == 0:
        print('Element Selection Failed')
        obj_list = [{'type':'Government','source':'Reuters Tech', 'title': 'Element Selection Failed', 'link': '', 'Notes': '', 'date': ''}]
        reuters_tech_df = pd.DataFrame(obj_list)
        return reuters_tech_df

    object_list = []
    ## Find all relevant tags
    for item in soup.find_all(class_=element):
        if datetime.strptime(item.find(class_='news-release-date').get_text(), '%b %d, %Y').strftime("%B %d, %Y") in date_list:
            title = item.find('a').get_text()
            ilink = item.find('a').get('href')
            notes = item.find()
            idate = item.find(class_='news-release-date').get_text()
            obj_data = {'type':'Government','source':'Agriculture Dept', 'title': title, 'link': ilink, 'Notes': '', 'date': idate}
            object_list.append(obj_data)
    ## Final dataframe is defined
    agriculture_dept_df = pd.DataFrame(object_list)

    ##** Error Handling for empty result
    if len(agriculture_dept_df) == 0:
        print('URL Broken')
        obj_list = [{'type':'Government','source':'Agriculture Dept', 'title': 'Data List Empty', 'link': '', 'Notes': '', 'date': ''}]
        agriculture_dept_df = pd.DataFrame(obj_list)
        return agriculture_dept_df
    ## Final Return Statement
    print(agriculture_dept_df)
    return agriculture_dept_df
        
agriculture_scrape()
        



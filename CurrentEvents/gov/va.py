from bs4 import BeautifulSoup  ## BeautifulSoup is a web parsing package to help pull specific HTML components
import pandas as pd 
from datetime import date, timedelta, datetime
import requests 

def va_scrape():
    ## Date List created with string values for the last 4 days to only pull opinions from that range.  
    ## General templates to pull from, not all are always used.
    today = date.today()
    year = today.strftime("%Y")
    month = today.strftime("%m")

    ## Headers is used because a User-Agent was required by the website
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.46'}
    link = "https://blogs.va.gov/VAntage/date/"+year+"/"+month+"/"

    ##** Error Handling for bad URL
    try:
        page = requests.get(link, headers=headers)
        page.raise_for_status()
    except:
        print('URL Broken')
        obj_list = [{'type':'Government','source':'VA Dept', 'title': 'Link Broken', 'link': '', 'Notes': '', 'date': ''}]
        va_dept_df = pd.DataFrame(obj_list)
        return va_dept_df
        
    ## Parse the webpage
    page = requests.get(link, headers=headers)
    soup = BeautifulSoup(page.content, 'lxml')

    ## Actual HTML pull
    object_list = []
    for item in soup.find_all('article'):

        title = item.find('h2').find('a').get_text()
        ilink = item.find('a').get('href')
        notes = item.find()
        idate = item.find(class_='updated rich-snippet-hidden').get_text()
        obj_data = {'type':'Government','source':'VA Dept', 'title': title, 'link': ilink, 'Notes': 'notes', 'date': idate}
        object_list.append(obj_data)

    ## Final dataframe is defined
    va_dept_df = pd.DataFrame(object_list)

    ##** Error Handling for empty result
    if len(va_dept_df) == 0:
        print('URL Broken')
        obj_list = [{'type':'Government','source':'VA Dept', 'title': 'Data List Empty', 'link': '', 'Notes': '', 'date': ''}]
        va_dept_df = pd.DataFrame(obj_list)
        return va_dept_df
    ## Final Return Statement
    return va_dept_df


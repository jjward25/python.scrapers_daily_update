from bs4 import BeautifulSoup  ## BeautifulSoup is a web parsing package to help pull specific HTML components
import urllib.request  ## to get a access to a URL and its content
import pandas as pd 
from datetime import date, timedelta, datetime
import requests 

def irs_scrape():
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
    print(date_list)
    ## Headers is used because a User-Agent was required by the website
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.46'}
    link = "https://www.irs.gov/newsroom"

     ##** Error Handling for bad URL
    try:
        page = requests.get(link, headers=headers)
        page.raise_for_status()
    except:
        print('URL Broken')
        obj_list = [{'type':'Government','source':'IRS', 'title': 'Link Broken', 'link': '', 'Notes': '', 'date': ''}]
        irs_df = pd.DataFrame(obj_list)
        return irs_df

    page = requests.get(link, headers=headers)
    soup = BeautifulSoup(page.content, 'lxml')

    ## Actual HTML pull
    object_list = []
    soup_nuts = soup.find_all('p')
    #print(soup_nuts[3])
    for item in soup_nuts[1:10]:
        #print("Item:")
        #print(item)
        title = ''
        ilink = ''
        notes = ''
        idate = ''
        if(type(item.find('a')) == type(None)):
            object_list[-1]['Notes']=item.get_text()
            object_list[-1]['Date']=item.get_text().partition(', ')[2].partition(' —')[0]
            pass
        else:
            #if item.find('span').get_text() in date_list:
            title = item.find('a').attrs["title"]
            ilink = 'https://www.irs.gov/' + item.find('a').get('href')
            obj_data = {'type':'Government','source':'IRS', 'title': title, 'link': ilink, 'Notes': notes, 'Date': idate}
            object_list.append(obj_data)
    ## Filter for Dates, pull most recent record if none within range to confirm query is still running
    filtered_list = [p for p in object_list if p['Date'] in date_list]
    if len(filtered_list) == 0:
        filtered_list = object_list[0]
    ## Final dataframe is defined
    irs_df = pd.DataFrame(filtered_list)
    #print(irs_df)

    ##** Error Handling for empty result
    if len(irs_df) == 0:
        print('No Result')
        obj_list = [{'type':'Government','source':'IRS', 'title': 'Data List Empty', 'link': '', 'Notes': '', 'date': ''}]
        irs_df = pd.DataFrame(obj_list)
        return irs_df
    ## Final Return Statement
    print(irs_df)
    irs_df.to_clipboard()
    return irs_df

irs_scrape()

## Requires Selenium
from datetime import date, timedelta
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
import time

chromedriver = "C:\\Users\\Joe\\Downloads\\chromedriver_win32\\chromedriver.exe"
option = webdriver.ChromeOptions()
option.binary_location = 'C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe'
s = Service(chromedriver)
driver = webdriver.Chrome(service=s, options=option)

## Date List created with string values for the last 4 days to only pull opinions from that range.  
## General templates to pull from, not all are always used.
today = date.today()
yesterday = date.today() - timedelta(1)
today_word = today.strftime("%B %d, %Y")
today_word_single_digit_day = today.strftime("%B %d, %Y").replace(" 0", " ")
yesterday_word = yesterday.strftime("%B %d, %Y")
yesterday_word_single_digit_day = yesterday.strftime("%B %d, %Y").replace(" 0", " ")
date_list = [today_word,yesterday_word,today_word_single_digit_day,yesterday_word_single_digit_day]    

try:
    ##** Error Handling for bad URL
    try:
        driver.get("https://www.bloomberg.com/search?query=the")
        #time.sleep(50)
    except:
        print('URL Broken')
        obj_list = [{'type':'STEMBiz','source':'Bloomberg', 'title': 'Driver or Link Issue', 'link': '', 'Notes': '', 'date': ''}]
        bloomberg_df = pd.DataFrame(obj_list)    
    ## Actual HTML pull
    object_list = [] 
    for item in driver.find_elements(By.CLASS_NAME,'headline__3a97424275'):
        #print(item)
        title = item.text
        ilink = item.get_attribute("href")
        #notes = item.find()
        #idate = item.find_element(By.TAG_NAME,"time").text[:-15]
        #print(idate)
        obj_data = {'type':'STEMBiz','source':'Bloomberg', 'title': title, 'link': ilink, 'Notes': '', 'date': 'idate'}
        object_list.append(obj_data)
        ## IF statement above pulls in anything within the listed date range.  Below checks if that received anything, and 
        ## is meant to pull in the most recent record if none are within the date range, so we know if the code is broken or if there's just nothing new
    if len(object_list) == 0:
        title = item.text
        ilink = item.get_attribute("href")
        #notes = item.find()
        #idate = item.find_element(By.TAG_NAME,"time").text[:-15]
        #print(idate)
        obj_data = {'type':'STEMBiz','source':'Bloomberg', 'title': title, 'link': ilink, 'Notes': 'Query Worked', 'date': 'idate'}
        object_list.append(obj_data)


    ## Final dataframe is defined
    bloomberg_df = pd.DataFrame(object_list)
    bloomberg_df = bloomberg_df

    ##** Error Handling for empty result
    if len(bloomberg_df) == 0:
        print('No Result')
        obj_list = [{'type':'STEMBiz','source':'Bloomberg', 'title': 'Data List Empty', 'link': '', 'Notes': '', 'date': ''}]
        bloomberg_df = pd.DataFrame(obj_list)

    print(bloomberg_df)
except:
    obj_list = [{'type':'STEMBiz','source':'Bloomberg', 'title': 'Suspicious Activity - Req Declined', 'link': '', 'Notes': '', 'date': ''}]
    bloomberg_df = pd.DataFrame(obj_list)
    print(bloomberg_df)

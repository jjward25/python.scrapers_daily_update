## Requires Selenium
from datetime import date, timedelta
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd

chromedriver = "C:\\Users\\Joe\\Downloads\\chromedriver_win32\\chromedriver.exe"
option = webdriver.ChromeOptions()
option.binary_location = 'C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe'
s = Service(chromedriver)
driver = webdriver.Chrome(service=s, options=option)

## Date List created with string values for the last 4 days to only pull opinions from that range.  
## General templates to pull from, not all are always used.
today = date.today()
yesterday = date.today() - timedelta(1)
two_ago = date.today() - timedelta(2)
today_word = today.strftime("%B %d, %Y").upper()
today_word_single_digit_day = today.strftime("%B %d, %Y").replace(" 0", " ").upper()
yesterday_word = yesterday.strftime("%B %d, %Y").upper()
yesterday_word_single_digit_day = yesterday.strftime("%B %d, %Y").replace(" 0", " ").upper()
date_list = [today_word,yesterday_word,today_word_single_digit_day,yesterday_word_single_digit_day]    
#print(date_list)
## Test that you're pulling the right object
#articles =  driver.find_elements(By.XPATH,'//div[@class="listing-with-preview item explore-item"]')
#print(articles[2].text)

##** Error Handling for bad URL
try:
    driver.get("https://www.foreignaffairs.com/search/")
except:
    print('URL Broken')
    obj_list = [{'type':'Op Ed','source':'CFR', 'title': 'Driver or Link Issue', 'link': '', 'Notes': '', 'date': ''}]
    foreign_affairs_df = pd.DataFrame(obj_list)    

## Actual HTML pull
object_list = [] 
for item in driver.find_elements(By.XPATH,'//article[@class="browse-list-item container"]')[0:10]:
    if item.find_element(By.CLASS_NAME,"publication-date").text in date_list:
        title = item.find_element(By.XPATH,'//h2[@class="title ls-0 mb-0 mt-2"]').text
        #print(title)
        ilink = item.find_element(By.TAG_NAME,"a").get_attribute("href")
        #notes = item.find()
        idate = item.find_element(By.CLASS_NAME,"publication-date").text
        #print(idate)
        obj_data = {'type':'Op Ed','source':'Foreign Affairs', 'title': title, 'link': ilink, 'Notes': '', 'date': idate}
        object_list.append(obj_data)
    ## IF statement above pulls in anything within the listed date range.  Below checks if that received anything, and 
    ## is meant to pull in the most recent record if none are within the date range, so we know if the code is broken or if there's just nothing new
if len(object_list) == 0:
    item = driver.find_element(By.XPATH,'//article[@class="browse-list-item container"]')
    title = item.find_element(By.XPATH,'//h2[@class="title ls-0 mb-0 mt-2"]').text
    #print(title)
    ilink = item.find_element(By.TAG_NAME,"a").get_attribute("href")
    #notes = item.find()
    idate = item.find_element(By.CLASS_NAME,"publication-date").text
    #print(idate)
    obj_data = {'type':'Op Ed','source':'Foreign Affairs', 'title': title, 'link': ilink, 'Notes': 'Query Worked', 'date': idate}
    object_list.append(obj_data)


## Final dataframe is defined
foreign_affairs_df = pd.DataFrame(object_list)
foreign_affairs_df = foreign_affairs_df

##** Error Handling for empty result
if len(foreign_affairs_df) == 0:
    print('No Result')
    obj_list = [{'type':'Op Ed','source':'Foreign Affairs', 'title': 'Data List Empty', 'link': '', 'Notes': '', 'date': ''}]
    foreign_affairs_df = pd.DataFrame(obj_list)

print(foreign_affairs_df)
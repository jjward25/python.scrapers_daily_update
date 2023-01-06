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
#driver.get("https://www.defense.gov/Newsroom/") ## Must run this somewhere before searching for elements.  In this case we run it in the Try/Except

## Date List created with string values for the last 4 days to only pull opinions from that range.  
## General templates to pull from, not all are always used.
today = date.today()
yesterday = date.today() - timedelta(1)
today_word = today.strftime("%B %d, %Y")
today_word_single_digit_day = today.strftime("%B %d, %Y").replace(" 0", " ")
yesterday_word = yesterday.strftime("%B %d, %Y")
yesterday_word_single_digit_day = yesterday.strftime("%B %d, %Y").replace(" 0", " ")
date_list = [today_word,yesterday_word,today_word_single_digit_day,yesterday_word_single_digit_day]    

## Test that you're pulling the right object
#articles =  driver.find_elements(By.XPATH,'//div[@class="listing-with-preview item explore-item"]')
#print(articles[2].text)

##** Error Handling for bad URL
try:
    driver.get("https://www.usda.gov/media/press-releases")
except:
    print('URL Broken')
    obj_list = [{'type':'Government','source':'USDA', 'title': 'Driver or Link Issue', 'link': '', 'Notes': '', 'date': ''}]
    agriculture_df = pd.DataFrame(obj_list)    

## Actual HTML pull
object_list = [] 
for item in driver.find_elements(By.XPATH,'//li[@class="news-releases-item"]'):
    #print(item)
    if item.find_element(By.CLASS_NAME,"news-release-date").text in date_list:
        title = item.find_element(By.TAG_NAME,"a").text
        #print(title)
        ilink = item.find_element(By.TAG_NAME,"a").get_attribute("href")
        #notes = item.find()
        idate = item.find_element(By.CLASS_NAME,"news-release-date").text
        #print(idate)
        obj_data = {'type':'Government','source':'USDA', 'title': title, 'link': ilink, 'Notes': '', 'date': idate}
        object_list.append(obj_data)
    ## IF statement above pulls in anything within the listed date range.  Below checks if that received anything, and 
    ## is meant to pull in the most recent record if none are within the date range, so we know if the code is broken or if there's just nothing new
if len(object_list) == 0:
    item = driver.find_element(By.XPATH,'//li[@class="news-releases-item"]')
    title = item.find_element(By.TAG_NAME,"a").text
    #print(title)
    ilink = item.find_element(By.TAG_NAME,"a").get_attribute("href")
    #notes = item.find()
    idate = item.find_element(By.CLASS_NAME,"news-release-date").text
    #print(idate)
    obj_data = {'type':'Government','source':'USDA', 'title': title, 'link': ilink, 'Notes': 'Query Working, No New Posts', 'date': idate}
    object_list.append(obj_data)


## Final dataframe is defined
agriculture_df = pd.DataFrame(object_list)
agriculture_df = agriculture_df.head()

##** Error Handling for empty result
if len(agriculture_df) == 0:
    print('No Result')
    obj_list = [{'type':'Government','source':'USDA', 'title': 'Data List Empty', 'link': '', 'Notes': '', 'date': ''}]
    agriculture_df = pd.DataFrame(obj_list)

print(agriculture_df)

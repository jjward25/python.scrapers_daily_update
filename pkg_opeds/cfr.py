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
today_word = today.strftime("%B %d, %Y").upper()
today_word_single_digit_day = today.strftime("%B %d, %Y").replace(" 0", " ")
yesterday_word = yesterday.strftime("%B %d, %Y").upper()
yesterday_word_single_digit_day = yesterday.strftime("%B %d, %Y").replace(" 0", " ")
date_list = [today_word,yesterday_word,today_word_single_digit_day,yesterday_word_single_digit_day]    
#print(date_list)
## Test that you're pulling the right object
#articles =  driver.find_elements(By.XPATH,'//div[@class="listing-with-preview item explore-item"]')
#print(articles[2].text)

##** Error Handling for bad URL
try:
    driver.get("https://www.cfr.org/")
except:
    print('URL Broken')
    obj_list = [{'type':'Op Ed','source':'CFR', 'title': 'Driver or Link Issue', 'link': '', 'Notes': '', 'date': ''}]
    cfr_df = pd.DataFrame(obj_list)
    
## Actual HTML pull
object_list = [] 
for item in driver.find_elements(By.XPATH,'//a[@class="card-article__link"]')[7:15]:
    title = item.find_element(By.TAG_NAME,'span').text
    #print(title)
    ilink = item.get_attribute("href")
    #notes = item.find()
    #idate = item.find_element(By.CLASS_NAME,"publication-date").text
    #print(idate)
    obj_data = {'type':'Op Ed','source':'CFR', 'title': title, 'link': ilink, 'Notes': '', 'date': 'idate'}
    object_list.append(obj_data)  


if len(object_list) == 0:
    obj_data = {'type':'Op Ed','source':'CFR', 'title': 'broken', '': 'ilink', 'Notes': '', 'date': ''}
    object_list.append(obj_data) 


## Final dataframe is defined
cfr_df = pd.DataFrame(object_list)

##** Error Handling for empty result
if len(cfr_df) == 0:
    print('No Result')
    obj_list = [{'type':'Op Ed','source':'CFR', 'title': 'Data List Empty', 'link': '', 'Notes': '', 'date': ''}]
    cfr_df = pd.DataFrame(obj_list)

print(cfr_df)
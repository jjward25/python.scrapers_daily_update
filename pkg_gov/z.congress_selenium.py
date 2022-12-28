## Requires Selenium
from datetime import date, timedelta, datetime
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

def congress_scrape():
    ## Date List created with string values for the last 4 days to only pull opinions from that range.  
    ## General templates to pull from, not all are always used.
    today = date.today()
    yesterday = date.today() - timedelta(1)
    two_ago = date.today() - timedelta(2)

    today_new = today.strftime("%m/%d/%Y")
    yesterday_new = yesterday.strftime("%m/%d/%Y")
    two_ago_new = two_ago.strftime("%m/%d/%Y")

    today_word = today.strftime("%B %d, %Y")
    today_word_single_digit_day = today.strftime("%B %d, %Y").replace(" 0", " ")
    yesterday_word = yesterday.strftime("%B %d, %Y")
    yesterday_word_single_digit_day = yesterday.strftime("%B %d, %Y").replace(" 0", " ")
    two_ago_word = two_ago.strftime("%B %d, %Y")
    two_ago_word_single_digit_day = two_ago.strftime("%B %d, %Y").replace(" 0", " ")
    date_list = [today_new,yesterday_new,two_ago_new,today_word,yesterday_word,two_ago_word,today_word_single_digit_day,yesterday_word_single_digit_day,two_ago_word_single_digit_day]    
    #print(date_list)
    
    ## Test that you're pulling the right object
    #articles =  driver.find_elements(By.XPATH,'//div[@class="listing-with-preview item explore-item"]')
    #print(articles[2].text)
    
    ##** Error Handling for bad URL
    try:
        driver.get("https://www.congress.gov/advanced-search/legislation?congresses%5B%5D=117&legislationNumbers=&restrictionType=field&restrictionFields%5B%5D=allBillTitles&restrictionFields%5B%5D=summary&summaryField=billSummary&enterTerms=&wordVariants=true&legislationTypes%5B%5D=hr&legislationTypes%5B%5D=hres&legislationTypes%5B%5D=hjres&legislationTypes%5B%5D=hconres&legislationTypes%5B%5D=hamdt&legislationTypes%5B%5D=s&legislationTypes%5B%5D=sres&legislationTypes%5B%5D=sjres&legislationTypes%5B%5D=sconres&legislationTypes%5B%5D=samdt&public=true&private=true&chamber=all&actionTerms=&legislativeActionWordVariants=true&dateOfActionOperator=equal&dateOfActionStartDate=&dateOfActionEndDate=&dateOfActionIsOptions=yesterday&dateOfActionToggle=multi&legislativeAction=Any&sponsorState=One&member=&sponsorTypes%5B%5D=sponsor&sponsorTypeBool=OR&dateOfSponsorshipOperator=equal&dateOfSponsorshipStartDate=&dateOfSponsorshipEndDate=&dateOfSponsorshipIsOptions=yesterday&committeeActivity%5B%5D=0&committeeActivity%5B%5D=3&committeeActivity%5B%5D=11&committeeActivity%5B%5D=12&committeeActivity%5B%5D=4&committeeActivity%5B%5D=2&committeeActivity%5B%5D=5&committeeActivity%5B%5D=9&satellite=[]&search=&submitted=Submitted&pageSort=latestAction%3Adesc")
    except:
        print('URL Broken')
        obj_list = [{'type':'Government','source':'Congress', 'title': 'Driver or Link Issue', 'link': '', 'Notes': '', 'date': ''}]
        defense_dept_df = pd.DataFrame(obj_list)
        return defense_dept_df
        
    #print(driver.find_elements(By.XPATH,'//li[@class="expanded"]')[1].text)
    ## Actual HTML pull
    object_list = [] 

    for item in driver.find_elements(By.XPATH,'//li[@class="expanded"]'):
        #print(item.text)
        try:
            cleandate = item.find_elements(By.CLASS_NAME,"result-item")[2].find_element(By.TAG_NAME,"span").text
        except:
            try:
                cleandate = item.find_elements(By.CLASS_NAME,"result-item")[3].find_element(By.TAG_NAME,"span").text
                print("Test 1 Triggered: Solution 1")
            except:
                cleandate = item.find_elements(By.CLASS_NAME,"result-item")[4].find_element(By.TAG_NAME,"span").text
                print("Test 1 Triggered: Solution 2")
        else:
            cleandate = item.find_elements(By.CLASS_NAME,"result-item")[2].find_element(By.TAG_NAME,"span").text
            print("Test 1 Passed")
        print("Cleandate: " + cleandate)

        # Trims the very unfriendly date element in several attempts
        # Tests (are the first 20 characters already a date? Are the first 10 characters after removing everything up to ": "?)
        try:
            datetime.strptime(cleandate[0:10],"%m/%d/%Y")
        except:
            print("Test 2: No Date Match")
        else: 
            cleandate = cleandate[0:10]
            print("Test 2 Triggered: First 10 Digits are a Date")
        
        try:
            datetime.strptime(cleandate.partition(': ')[2][0:10],"%m/%d/%Y")
        except:
            print("Test 3: No Date Match")
        else:
            cleandate = cleandate.partition(': ')[2][0:10]
            print("Test 3 Triggered: Date found after partitioning on a colon")

        try:
            datetime.strptime(cleandate.partition(': ')[2].partition('- ')[2][0:10],"%m/%d/%Y")
        except:
            print("Test 4: No Date Match")
        else:
            cleandate = cleandate.partition(': ')[2].partition('- ')[2][0:10]
            print("Test 4 Triggered: Date found after partitioning on a colon then a hyphen")

        try:
            datetime.strptime(cleandate.partition('- ')[2][0:10],"%m/%d/%Y")
        except:
            print("Test 5: No Date Match")
        else:
            cleandate = cleandate.partition('- ')[2][0:10]
            print("Test 5 Triggered: Date found after partitioning on a hypen")
      
        print("cleandate new: " + cleandate)

        if cleandate in date_list:
            title = item.find_element(By.CLASS_NAME,"result-title").text
            #print(title)
            ilink = item.find_element(By.TAG_NAME,"a").get_attribute("href")
            #notes = item.find()
            idate = cleandate
            #print(idate)
            obj_data = {'type':'Government','source':'Congress', 'title': title, 'link': ilink, 'Notes': '', 'date': idate}
            object_list.append(obj_data)
        ## IF statement above pulls in anything within the listed date range.  Below checks if that received anything, and 
        ## is meant to pull in the most recent record if none are within the date range, so we know if the code is broken or if there's just nothing new
    
    if len(object_list) == 0:
        item = driver.find_element(By.XPATH,'//li[@class="expanded"]')
        title = item.find_element(By.CLASS_NAME,"result-title").text
        #print(title)
        ilink = item.find_element(By.TAG_NAME,"a").get_attribute("href")
        #notes = item.find()
        idate = cleandate
        #print(idate)
        obj_data = {'type':'Government','source':'Congress', title: 'title', 'link': ilink, 'Notes': '', 'date': idate}
        object_list.append(obj_data)

    ## Final dataframe is defined
    defense_dept_df = pd.DataFrame(object_list)
    defense_dept_df = defense_dept_df

    ##** Error Handling for empty result
    if len(defense_dept_df) == 0:
        print('No Result')
        obj_list = [{'type':'Government','source':'Defense Dept', 'title': 'Data List Empty', 'link': '', 'Notes': '', 'date': ''}]
        defense_dept_df = pd.DataFrame(obj_list)
        return defense_dept_df

    print(defense_dept_df)
    return defense_dept_df
    
congress_scrape()
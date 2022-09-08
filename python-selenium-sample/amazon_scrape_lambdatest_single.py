# google-search-lambdatest.py

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import os
import pandas as pd

import csv


"""
    LambdaTest selenium automation sample example
    Configuration
    ----------
    username: Username can be found at automation dashboard
    accessToken:  AccessToken can be genarated from automation dashboard or profile section

    Result
    -------
    Execute Test on lambdatest Distributed Grid perform selenium automation based 
"""

# username: Username can be found at automation dashboard
username = os.getenv("makwanashyamal96")
# accessToken:  AccessToken can be genarated from automation dashboard or profile section
accessToken = os.getenv("1BJJ8UAUzbnzNdkttNNaXVPG2sITjbPiGoF5ydAowcx3kZcItu")
# gridUrl: gridUrl can be found at automation dashboard
gridUrl = "hub.lambdatest.com/wd/hub"


capabilities = {
    'LT:Options': {
        "build": "Chrome test",
        "name": "Single Chrome test",
        "platformName": "Windows 10",
        "terminal": 'true',
        "console": 'true'
    },
    "browserName": "Chrome",
    "browserVersion": "latest",
}


#url = "https://"+username+":"+accessToken+"@"+gridUrl
url = "https://makwanashyamal96:1BJJ8UAUzbnzNdkttNNaXVPG2sITjbPiGoF5ydAowcx3kZcItu@hub.lambdatest.com/wd/hub"


"""
    ----------
    platformName : Supported platfrom - (Windows 10, Windows 8.1, Windows 8, Windows 7,  macOS High Sierra, macOS Sierra, OS X El Capitan, OS X Yosemite, OS X Mavericks)
    browserName : Supported platfrom - (chrome, firefox, Internet Explorer, MicrosoftEdge)
    browserVersion :  Supported list of version can be found at https://www.lambdatest.com/capabilities-generator/

    Result
    -------
"""

driver = webdriver.Remote(
    command_executor=url,
    desired_capabilities=capabilities
)

"""
    ----------
    Execute test:  navigate google.com search LambdaTest
    Result
    ----------
    print title
"""

# driver.get("https://www.google.com/ncr")

# print("Searching lambdatest on google.com ")
# time.sleep(8)
# elem = driver.find_element_by_name("q")
# elem.send_keys("lambdatest.com")
# elem.submit()

# print("Printing title of current page :"+driver.title)
# driver.execute_script("lambda-status=passed")
# print("Requesting to mark test : pass")


driver.get('https://www.amazon.in')
driver.maximize_window()


# get the input elements
input_search = driver.find_element_by_xpath("//*[@id='twotabsearchtextbox']")
time.sleep(3)  
search_button = driver.find_element_by_xpath("//*[@id='nav-search-submit-button']")
# input_search = browser.find_element_by_id("//*[@id='twotabsearchtextbox']")
# search_button = browser.find_element_by_xpath("(//input[@type='submit'])[1]")


# send the input to the webpage
input_search.send_keys("iphone 13")
time.sleep(1)
search_button.click()


products = []
# product_text = []
# price_text = []
prices = []
for i in range(2):
#     print('Scraping page', i+1)
    product = driver.find_elements_by_xpath("//span[@class='a-size-medium a-color-base a-text-normal']")
#     product_text = product.get_attribute("innerHTML")

    price = driver.find_elements_by_xpath("//span[@class='a-price-whole']")   #a-offscreen
    
#     for my_href2 in price:
#         price_text.append(my_href2.get_attribute("innerHTML"))        


#     for my_href1 in product:
#         product_text.append(my_href1.get_attribute("innerHTML"))
            
    
    
#     print (product)
    for p in product:
        products.append(p.text)        
        
    for q in price:        
        prices.append(q.text)        

        
    next_button = driver.find_element_by_xpath("//a[@class='s-pagination-item s-pagination-next s-pagination-button s-pagination-separator']")
    next_button.click()
    time.sleep(2)
    
data = pd.DataFrame()
data['product name'] = products
data['Price'] = prices
data['Price'] = data['Price'].astype(str)
print (data)

# data.to_excel('product_price.xls', index=False)

"""
    Quit selenium driver
"""
driver.quit()
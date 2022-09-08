from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import os, sys, json, time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import pandas as pd


json_name = sys.argv[1]
# username: Username can be found at automation dashboard
username = os.getenv("makwanashyamal96")
# accessToken:  AccessToken can be genarated from automation dashboard or profile section
accessToken = os.getenv("1BJJ8UAUzbnzNdkttNNaXVPG2sITjbPiGoF5ydAowcx3kZcItu")
# gridUrl: gridUrl can be found at automation dashboard
gridUrl = "hub.lambdatest.com/wd/hub"

with open(json_name, "r") as f:
    obj = json.loads(f.read())

instance_caps= obj[int(sys.argv[2])]
print ("Test "+sys.argv[2]+" started")

#------------------------------------------------------#
# Mention any other capabilities required in the test

#------------------------------------------------------#

caps = dict(instance_caps.items())
print (caps)
# caps = Merge(dict(caps.items()),dict(instance_caps.items()))

#------------------------------------------------------#
# THE TEST TO BE RUN PARALLELY GOES HERE
url = "https://makwanashyamal96:1BJJ8UAUzbnzNdkttNNaXVPG2sITjbPiGoF5ydAowcx3kZcItu@hub.lambdatest.com/wd/hub"
driver = webdriver.Remote(command_executor=url,desired_capabilities=caps)
try:
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
    for i in range(1):
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


finally:
    driver.quit()

import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class crawledArticle():
    def __init__(self,title,price):
        self.title=title
        #self.rating=rating
        self.price=price

class b:

    def article(self, name):
        count = 1
        page = 1
        pageIncrement = 1
        maxRetrieves = 10

        a = []

        #url = "https://www.amazon.com/" + name + "&page=" + str(page)
        url = "https://www.amazon.in/"

        options = Options()
        options.headless = False
        options.add_experimental_option("detach", True)
        browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        browser.maximize_window()
        browser.get(url)
        browser.set_page_load_timeout(10)      

        while True:
            try:
                if pageIncrement*page > maxRetrieves:
                    break
                
                if count > pageIncrement:
                    count = 1
                    page += 1

                # Get Title
                xPathTitle = '//*[@id="search"]/div[1]/div[2]/div/span[3]/div[2]/div[' + str(count) + ']/div/span/div/div/div[2]/div[2]/div/div[1]/div/div/div[1]/h2/a/span'
                title = browser.find_element_by_xpath(xPathTitle)
                titleText = title.get_attribute("innerHTML").splitlines()[0]
                title.click()
                
                # Get Price
                xPathPrice = '//*[@id="corePrice_desktop"]/div/table/tbody/tr[2]/td[2]/span[1]/span[2]'                
                

                price = browser.find_element_by_xpath(xPathPrice)
                priceText = price.get_attribute("innerHTML")

                url = "https://www.amazon.com/s?k=iphone+13&page=" + str(page)
                browser.get(url)
                browser.set_page_load_timeout(10) 

                info = crawledArticle(titleText, priceText)
                a.append(info)
                
                count += 1

            except Exception as e:
                # print("Exception On Count", count, e)
                count += 1

                if pageIncrement*page > maxRetrieves:
                    break
                
                if count > pageIncrement:
                    count = 1
                    page += 1

                url = "https://www.amazon.com/s?k=iphone+13&page=" + str(page)
                browser.get(url)
                browser.set_page_load_timeout(10) 


        #browser.close()

        return a
    # print (a)
        


fetcher = b()

#for article in fetcher.article("iphone 13"):
#    print ([article.title,article.price])
#fetcher.article("iphone 13")
    

#with open('pro.csv', 'w', newline='', encoding='utf-8') as csvfile:
#    articlewriter = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#    for article in fetcher.article("iphone 13"):
#        articlewriter.writerow([article.title,article.price])

with open('pro.csv', 'w', encoding='UTF8') as csvfile:
    articlewriter = csv.writer(csvfile)
    for article in fetcher.article("iphone 13"):
        print ([article.title,article.price])
        articlewriter.writerow([article.title,article.price])        
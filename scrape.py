from flask import jsonify
from selenium import webdriver
#from bs4 import BeautifulSoup as soup
from selenium.webdriver.chrome.options import Options
import bs4
import os


class WebScrapper:

      productListUrl = 'https://www.walmart.ca/search/'

      def __init__(self, upc):
            self.productListUrl = self.productListUrl + upc
    
      


      def getProductUPC(self):
            # In order to get the page loaded using JavaScript, we need a web driver
            
#            chrome_options = Options()
#            chrome_options.binary_location = GOOGLE_CHROME_BIN
#            chrome_options.add_argument('--disable-gpu')
#            chrome_options.add_argument('--no-sandbox')
#            browser = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)
            #chrome_exec_shim = os.environ.get("GOOGLE_CHROME_BIN", "chromedriver")
            #self.selenium = webdriver.Chrome(executable_path=chrome_exec_shim)
            #driver = webdriver.Chrome()
            #browser = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, 
            #chrome_options=chrome_options)
            
            
            GOOGLE_CHROME_BIN = '/app/.apt/opt/google/chrome/chrome'
            GOOGLE_CHROME_SHIM = '/app/.apt/usr/bin/google-chrome-stableand'
            CHROMEDRIVER_PATH = '/app/.chromedriver/bin/chromedriver'
            #chrome_bin = os.environ.get('GOOGLE_CHROME_BIN', "chromedriver")
            chrome_bin = os.environ.get('GOOGLE_CHROME_SHIM', None)
            options = webdriver.ChromeOptions()
            options.binary_location = chrome_bin
            options.add_argument('--no-sandbox')
            options.add_argument('headless')
            options.add_argument('start-maximized'); 
            options.add_argument('disable-infobars'); 
            options.add_argument('--disable-extensions'); 
            options.add_argument('--disable-dev-shm-usage');
            
            browser = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=options)
#            temp=browser.get(self.productListUrl)
            temp=browser.get('https://www.walmart.ca/search/6000020342793')
            
            #browser.set_page_load_timeout(60)
            #ele=browser.find_element_by_css_selector('#thumb-10045875 > a > div.product-details-container > span.all-price-sections > div.price-current > div:nth-child(1)')
#            page = browser.execute_script("return document.documentElement.outerHTML")
            browser.close()
            browser.quit()
#
#            # Get the bs4 library to parse it as HTML
#            #page_soup = soup(page, "html.parser")
#            page_soup=bs4.BeautifulSoup(page,'html.parser')
#            
#            # Get the required div in the container varibale
#            container = page_soup.findAll("a", { "class" : "product-link" })
#
#            # Validation not in place yet
#            print(container)
            return jsonify({ "ERROR" : str(productListUrl) })
#            if len(container) > 0:
#
#                  if len(container) > 1:
#                        # More than one product with the same UPC was found
#                        return jsonify({ "ERROR" : "MANY" })
#                  else:
#                        # Only one product was found
#                        # Get the image
#                        image_url = page_soup.findAll("img", { "class" : "image" })
#                        image_url = 'https://' + image_url[0]["src"]
#                        # Get the title
#                        title = page_soup.findAll("h2", { "class" : "thumb-header"})
#                        title = title[0].text
#                        # Get the price
#                        price = page_soup.findAll("div", { "class" : "price-current" })
#                        price = price[0].text.strip()
#
#                        # print(image_url + '\n' + title + '\n' + price)
#
#                        return jsonify({"image_url" : image_url, "title" : title, "price" : price})
#
#            else:
#                  # Send an error code
#                  return jsonify({ "ERROR" : "No data" })

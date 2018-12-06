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
    
      def getAmazonPrice(productUrl):
            res=requests.get(productUrl)
            res.raise_for_status()
            soup=bs4.BeautifulSoup(res.text,'html.parser')
            ele=soup.select('#product-purchase-cartridge > div.pricing-shipping > div.pricing.wgrid-3w6.wgrid-2w4.marg-l-0 > div.price-current > div:nth-child(1)')
            return ele[0].text.strip()
    


      def getProductUPC(self):
            # In order to get the page loaded using JavaScript, we need a web driver
            GOOGLE_CHROME_BIN = '/app/.apt/opt/google/chrome/chrome'
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
            CHROMEDRIVER_PATH = '/app/.chromedriver/bin/chromedriver'

            chrome_bin = os.environ.get('GOOGLE_CHROME_BIN', "chromedriver")
            options = webdriver.ChromeOptions()
            options.binary_location = chrome_bin
            options.add_argument("--disable-gpu")
            options.add_argument("--no-sandbox")
            options.add_argument('headless')
            options.add_argument('window-size=1200x600')
            browser = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=options)
            browser.get(self.productListUrl)
            page = browser.execute_script("return document.documentElement.outerHTML")
            browser.close()
            browser.quit()

            # Get the bs4 library to parse it as HTML
            #page_soup = soup(page, "html.parser")
            page_soup=bs4.BeautifulSoup(page,'html.parser')
            
            # Get the required div in the container varibale
            container = page_soup.findAll("a", { "class" : "product-link" })

            # Validation not in place yet
            print(container)
            return jsonify({ "ERROR" : str(page) })
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

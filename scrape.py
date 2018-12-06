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
            return container
            
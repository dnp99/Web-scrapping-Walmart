from flask import jsonify
from selenium import webdriver
#from bs4 import BeautifulSoup as soup
import bs4

class WebScrapper:

      productListUrl = 'https://www.walmart.ca/search/'

      def __init__(self, upc):
            self.productListUrl = self.productListUrl + upc

      def getProductUPC(self):
            # In order to get the page loaded using JavaScript, we need a web driver
            browser = webdriver.Chrome(executable_path=r"D:\chromedriver_win32\chromedriver.exe")
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

            if len(container) > 0:

                  if len(container) > 1:
                        # More than one product with the same UPC was found
                        return jsonify({ "ERROR" : "MANY" })
                  else:
                        # Only one product was found
                        # Get the image
                        image_url = page_soup.findAll("img", { "class" : "image" })
                        image_url = 'https://' + image_url[0]["src"]
                        # Get the title
                        title = page_soup.findAll("h2", { "class" : "thumb-header"})
                        title = title[0].text
                        # Get the price
                        price = page_soup.findAll("div", { "class" : "price-current" })
                        price = price[0].text.strip()

                        # print(image_url + '\n' + title + '\n' + price)

                        return jsonify({"image_url" : image_url, "title" : title, "price" : price})

            else:
                  # Send an error code
                  return jsonify({ "ERROR" : "NONE" })

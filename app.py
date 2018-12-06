from flask import Flask
from scrape import WebScrapper
app = Flask(__name__)

@app.route('/')
def hello_world():
      return 'Hello, World!'

@app.route('/upc/<upc_code>')
def getProductUPC(upc_code):

      web = WebScrapper(upc_code)  
      return web.getAmazonPrice('https://www.walmart.ca/en/ip/6000017348230')
    #      return web.getProductUPC()

if __name__ == "__main__":
    app.run()
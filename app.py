from flask import Flask
from scrape import WebScrapper
app = Flask(__name__)

@app.route('/')
def hello_world():
      return '[{"image_url":"https:////i5.walmartimages.ca/images/Thumbnails/272/437/999999-6923052272437.jpg?odnBound=200","price":"$12","title":"Casemate Paper Composition Book"},{"image_url":"https:////i5.walmartimages.ca/images/Thumbnails/093/915/6000199093915.jpg?odnBound=200","price":"$178","title":"Sanyo, 32\" Roku TV (FW32R19FC)"},{"image_url":"https:////i5.walmartimages.ca/images/Thumbnails/931/292/6000198931292.jpg?odnBound=200","price":"$2000","title":"Sharp AQUOS 40\" Class FHD (1080P) Smart LED TV (LC40P5000U)"}]'

@app.route('/upc/<upc_code>')
def getProductUPC(upc_code):

    web = WebScrapper(upc_code)  
    return web.getProductUPC()

if __name__ == "__main__":
    app.run()
from flask import Flask
from selenium import webdriver

app = Flask(__name__)

@app.route('/')
def hello_world():
      return 'Hello, Deep!'

if __name__ == "__main__":
    app.run()
    
chrome_options = Options()
chrome_options.binary_location = GOOGLE_CHROME_BIN
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, 
chrome_options=chrome_options)


driver.get('https://automatetheboringstuff.com')
html = browser.page_source
print html
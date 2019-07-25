from selenium import webdriver
browser=webdriver.Firefox()
browser.get('https://www.walmart.ca/search/6000020342793')
ele=browser.find_element_by_css_selector('#thumb-10045875 > a')
print(ele.text)




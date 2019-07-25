from selenium import webdriver

browser=webdriver.Firefox()
browser.get('https://www.walmart.ca/en/ip/6000017348230')
ele=browser.find_element_by_css_selector('#product-purchase-cartridge > div.pricing-shipping > div.pricing.wgrid-3w6.wgrid-2w4.marg-l-0 > div.price-current > div:nth-child(1)')
print(ele.text)

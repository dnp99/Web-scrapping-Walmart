import bs4,requests

def getAmazonPrice(productUrl):
    res=requests.get(productUrl)
    res.raise_for_status()
    soup=bs4.BeautifulSoup(res.text,'html.parser')
    ele=soup.select('#product-purchase-cartridge > div.pricing-shipping > div.pricing.wgrid-3w6.wgrid-2w4.marg-l-0 > div.price-current > div:nth-child(1)')
    return ele[0].text.strip()
    




price=getAmazonPrice('https://www.walmart.ca/en/ip/6000017348230')
print ('Price is ='+price)

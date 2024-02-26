from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://shopus.recaro-automotive.com/us/dynamic/?p=1'

#opening up connection , grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

#html parsing
page_soup = soup(page_html, "html.parser")
container = page_soup.findAll("div", {"class": "product-slider--item"})

#looping though product title
for containers in container:
    title = containers.div.div.a["title"]

    price_container = containers.findAll("span", {"class" : "price--default is--nowrap"})
    product_price = price_container[0].text.strip()

    print("title: "  + title)
    print("product_price: " + product_price) 
    
import time

from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

url = "https://www.footlocker.com/category/sale/mens.html?query=%3Arelevance%3AstyleDiscountPercent%3ASALE%3Agender%3A200000%3Abrand%3APUMA"

driver = webdriver.Chrome("chromedriver")
driver.get(url)

html = driver.page_source
soup = bs(html, "html.parser")

# finds all the <a> tag with class => ProductCard-link ProductCard-content , from this list extract "href".
# href is a relative value, so we will add "https://www.footlocker.com+href"

product_urls = soup.find_all('a', attrs={"class": "ProductCard-link ProductCard-content"})

# here we declare a list where we will store full URL, https://www.footlocker.com+href
product_urls_full = []

for product_url in product_urls:
    try:
        product_urls_full.append("https://www.footlocker.com" + product_url['href'])
    except KeyError:
        pass

# pass the product URL 1 by 1
for product_url_full in product_urls_full:

    driver = webdriver.Chrome("/Users/ak054561/chromedriver")
    driver.get(product_url_full)
    wait = WebDriverWait(driver, 30)
    html = driver.page_source
    soup = bs(html, "html.parser")

    print("URL Requested" + product_url_full)

    span_tag = soup.find('span', attrs={"class": "ProductName-primary"})
    print("Product Name: " + span_tag.text)

    span_tag = soup.find('span', attrs={"class": "ProductPrice-original"})
    print("Product Original: " + span_tag.text)

    span_tag = soup.find('span', attrs={"class": "ProductPrice-final"})
    print("Product Final: " + span_tag.text)

    time.sleep(10)
from selenium import webdriver
from bs4 import BeautifulSoup
import time

def getprice(url):
    product_code = get_shopee_productcode(url)
    driver = webdriver.Chrome(".\chromedriver.exe")
    driver.get(url)
    time.sleep(5)
    content = driver.page_source
    soup = BeautifulSoup(content,features="html.parser")
    price_curr = str(soup.find('div', attrs={'class': '_2Shl1j'}))
    if price_curr == "None":
        driver.quit()
        print("Error, try again")
        return getprice(url)

    price_string = price_curr.split(">")[1].split("<")[0]
    currency = price_string[0]
    price = price_string[1:len(price_string)]
    price_curr_json = {"price": price,
    "currency": currency,
    "item": product_code
    }
    return price_curr_json
    #write_response_tofile(content, product_code)


def write_response_tofile(response, product_code):
    html_file = "product code - " + product_code + ".html"

    with open(html_file, "w", encoding="utf-8") as f:
        f.write(response)
    return html_file

def get_shopee_productcode(url):
    item_code =  url.split("-i.")[1].split("?")[0]
    product_name = url.split("-i.")[0].split("/")[-1][:200]
    product_code = product_name + "-i." + item_code
    return product_code
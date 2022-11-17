#pip install slack_sdk, aiohttp, selenium, bs4, requests

import requests
from bs4 import BeautifulSoup
import json

def get_asin(url):
    asin = url.split('/')
    for i, dp in enumerate(asin):
        if dp == "dp":
            return (asin[i+1])

def get_domain(url):
    uri = url.split('/')
    for i in uri:
        if "amazon" in i:
            return i
    print("not supported, amazon only")
    exit()

def get_itemcode(url):
    return get_asin(url)

def getprice_amazon(parse_html):
    parse_price = parse_html.find(id="twister-plus-price-data-price")
    parse_curr = parse_html.find(id="twister-plus-price-data-price-unit")

    if parse_price == None:
        item_price = "none found"
        currency = "none found"
    else:
        item_price = parse_price.get("value")
        currency = parse_curr.get("value")

    return item_price, currency

def read_html(html_file):
    with open(html_file, "r", encoding="utf-8") as f:
        content = f.read()

    parse_html = BeautifulSoup(content,"html.parser", multi_valued_attributes=None)
    item_price, currency = getprice_amazon(parse_html)

    return item_price, currency


def send_request(s, prepared):
    response = s.send(prepared)
    return response

def write_response_tofile(response, item_code):
    html_file = "ASIN - " + item_code + ".html"

    with open(html_file,"w", encoding="utf-8") as f:
        f.write(response.text)
    return html_file

def pretty_print_POST(req):
    print('{}\n{}\r\n{}\r\n\r\n{}'.format(
        '-----------START-----------',
        req.method + ' ' + req.url,
        '\r\n'.join('{}: {}'.format(k, v) for k, v in req.headers.items()),
        req.body,
    ))

def getprice(url):
    domain = get_domain(url)
    item_code = get_itemcode(url)

    headers = {'authority' :'www.amazon.com', 'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36'}
    req = requests.Request("GET", url, headers=headers)
    prepared = req.prepare()
    s = requests.Session()
    pretty_print_POST(prepared)

    response = send_request(s, prepared)
    #print(response.text)
    #print(response.status_code)
    html_file = write_response_tofile(response, item_code)
    price_curr =  read_html(html_file)
    price = price_curr[0]
    currency = price_curr[1]
    price_curr_json = {"price": price,
    "currency": currency,
    "item": item_code}
    return price_curr_json
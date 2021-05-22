import requests
from bs4 import BeautifulSoup
import re

iphone_screen = requests.get("https://www.coalandcanary.com/shop").text

bs_iphone_screen = BeautifulSoup(iphone_screen, 'lxml')

search_results = bs_iphone_screen.find("ul", class_='_3Xnzg _3g8J4')

all_items = search_results.find_all('li')

fileName = "products.csv"

f = open(fileName, "w")

headers = "name, price\n"

f.write(headers)

print len(all_items)

for item in all_items:
    name = item.find('h3').text
    if item.find('span', {'data-hook': 'product-item-out-of-stock'}):
        price = item.find('span', {'data-hook': 'product-item-out-of-stock'}).text
    else:
        price = item.find('span', {'data-hook': 'product-item-price-to-pay'}).text

    f.write(str(name) + "," + price + "\n")

f.close()









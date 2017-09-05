from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
from datetime import datetime

stock='http://www.bloomberg.com/quote/EURUSD:CUR'
page=urlopen(stock)
soup=BeautifulSoup(page,'html.parser')

name_box = soup.find('h1', attrs={'class': 'name'})
name=name_box.text.strip()
print(name)

price_box = soup.find('div', attrs={'class':'price'})
price = price_box.text
print(price)

with open('stock.csv','a') as csv_file:
    writer=csv.writer(csv_file)
    writer.writerow([name,price,datetime.now()])

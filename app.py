# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests

quote_page = 'http://www.bloomberg.com/quote/SPX:IND'

html_doc = requests.get(quote_page)

#soup = BeautifulSoup(html_doc.text, 'html.parser')
soup = BeautifulSoup(html_doc.text, 'html.parser')

name = soup.find('h1')
quote = soup.select('div[class=schema-org-financial-quote]')

print(name)
print(quote)

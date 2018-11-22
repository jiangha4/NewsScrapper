# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import urllib2

html_doc = requests.get('http://www.bloomberg.com/quote/SPX:IND')

soup = BeautifulSoup(html_doc.text, 'html.parser')

# Take out the <div> of name and get its value
# name_box = soup.find('h1', attrs={'class': 'name'})
# name = name_box.text.strip()
# print name

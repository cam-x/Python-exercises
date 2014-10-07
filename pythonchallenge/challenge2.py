__author__ = 'Jianqiao'

import requests

from bs4 import BeautifulSoup

import re

response =  requests.get('http://www.pythonchallenge.com/pc/def/ocr.html')
soup = BeautifulSoup(response.text)

comments = soup.find_all(text=re.compile("%%") )
riddle = comments[0]
static_dict = dict()
for i in riddle:
    if i is not '\n':
        if i in static_dict:
            static_dict[i] += 1
        else:
            static_dict[i] = 1
print(static_dict)

text = []
for k,v in static_dict.items():
    if v == 1:
        text.append(k)

for i in riddle:
    if i in text:
        print(i, end='')

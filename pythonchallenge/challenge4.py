__author__ = 'Jianqiao'

import re
import requests

url_base = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
url_number = '63579'
url_next = url_base + url_number
response = requests.get(url_next)  # requests.get() returns a string data type of the source page.

p_number = re.compile('\d+')               # "+" means 1 or more something
url_number = ''.join(p_number.findall(response.text)) # parameter must be a string data type.
print(url_number)
p_text = re.compile('\D+')    # "\D" means not number(!=\d)
text = ''.join(p_text.findall(response.text))
while response.text == text + url_number:
    response = requests.get(url_next)
    url_number = ''.join(p_number.findall(response.text))
    url_next = url_base + url_number
    print(url_next)
print(response.text)

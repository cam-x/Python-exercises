__author__ = 'Jianqiao'

import re
import requests

response = requests.get('http://www.pythonchallenge.com/pc/def/equality.html')
#p = re.compile('(?<![A-Z])[A-Z]{3}[a-z][A-Z]{3}(?![A-Z])')
p = re.compile('[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]')  # Using () to catch what ww want, it's better than above.
text = p.findall(response.text)
answer = ''.join(text)
print(answer)


# list -> str : ''.join(my_list)
# str -> list : my_str.split()

__author__ = 'Jianqiao'

import requests
import pickle

riddle = requests.get('http://www.pythonchallenge.com/pc/def/banner.p') # riddle is NOT a string ! is a Object!
text_pickle = riddle.text.encode()     # riddle.text is a string! .encode() transform a string into a bytes data type.
text = pickle.loads(text_pickle)
for list_in_text in text:
    for tuple_in_list in list_in_text:
        print(tuple_in_list[0]*tuple_in_list[1], end='')
    print()

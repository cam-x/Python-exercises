__author__ = 'Jianqiao'
#a = [1, 11, 21, 1211, 111221,
""" Firstly, I thought it was three-base sequence. But, there is no Zero.
def three_to_ten(three):
    three_str = str(three)
    ten = 0
    for i in range(len(three_str)):
        ten += int(three_str[i])*3**(len(three_str) - 1 - i)
    return print('Three-base -> ', three, 'decimal -> ', ten)
three_to_ten(21)
"""
import re

a = [1]
p = re.compile(r'(\d)\1*')
for i in range(30):
    find = p.finditer(str(a[i]))
    new_str = ''
    for item in find:
        new_str += str(len(item.group())) + item.group(1)
    a.append(int(new_str))
print('len(a[30])->', len(str(a[30])))

print(a[:8])


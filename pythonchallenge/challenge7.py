__author__ = 'Jianqiao'

from PIL import Image

im = Image.open('oxygen.png')

pix_position_list = []

# Get the (x,y) position of black-white band
for i in range(im.size[0]):
    for j in range(im.size[1]):
        pix = im.getpixel((i,j))
        # RGB - when R_value == G_value == B_value, it's a black-and-white image.
        if pix[0] == pix[1] == pix[2]:
           pix_position_list.append([i,j])

"""
# Result -> x:{0,607} y:{43,51}
for i in pix_position_list:
    print(i)
"""
# Choose the line (i,43) and transform every pixel value into ascii.
# Unicode - a character-encoding scheme: Characters -> Integers.
# RGB color mode - red, green, blue, each color has 256 intensity. using a tuple (r, g, b) represent.

# Make a mapping: RGB (256) -> Unicode character
pix_value_unicode = []
for i in range(608):
    # chr(i) function: return the string representing a character whose Unicode codepoint is the
    # integer i.
    pix_value_unicode.append(chr(im.getpixel((i,43))[0]))
text = ''.join(pix_value_unicode)
print(text)

# In the text, We find every character repeats 7 times except the first letter 's'
print('s', end='')
for i in range(86):
    print(text[5 + 7*i], end='')
print()
hit_list = [105, 110, 116, 101, 103, 114, 105, 116, 121]
"""
# At first, I thought it was the position pixel in black-and-white band.
answer_list = []
for i in hit_list:
    answer_list.append(chr(im.getpixel((i,43))[0]))
answer = ''.join(answer_list)
print(answer)
"""
# In fact, it's Unicode.
print(''.join(chr(i) for i in hit_list))


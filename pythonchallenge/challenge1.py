__author__ = 'Jianqiao'

# Level 1
"""
def letter_change(sentence):
    for letter in sentence:
        if letter == 'm':
            letter = 'k'
            print('find letter m ', letter)
        elif letter == 'q':
            letter = 'o'
        elif letter == 'g':
            letter = 'e'
    return sentence
"""
"""
def letter_change(sentence):
    new_sentence = []
    for letter in sentence:
        if letter == 'k':
            new_sentence.append('m')
        elif letter == 'o':
            new_sentence.append('q')
        elif letter == 'e':
            new_sentence.append('g')
        else:
            new_sentence.append(letter)
    return new_sentence
"""
def letter_change(sentence):
    new_sentence=[]
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_list = sorted(list(alphabet))
    for letter in sentence:
        if letter in alphabet_list:
            if letter == 'x':
                new_sentence.append('z')
            elif letter == 'y':
                new_sentence.append('a')
            elif letter == 'z':
                new_sentence.append('b')
            else:
                new_sentence.append(alphabet_list[alphabet_list.index(letter) + 2])
        else:
            new_sentence.append(letter)
    return new_sentence

riddle = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb \
rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

"""
#riddle = 'map'
new_riddle = letter_change(list(riddle))
for i in new_riddle:
    print(i, end='')
"""


trans = str.maketrans('abcdefghijklmnopqrstuvwxyz', 'cdefghijklmnopqrstuvwxyzab')
print(riddle.translate(trans))


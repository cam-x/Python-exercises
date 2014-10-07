__author__ = 'Jianqiao'
# These simple exercises come from the link below:
# http://www.ling.gu.se/~lager/python_exercises.html

# Very simple exercises

# 1.Define a function max() that takes two numbers as arguments and returns the largest of them.
# Use the if-then-else construct available in Python.

def max_of_two(num_1, num_2):
    if num_1 > num_2:
        return num_1
    else:
        return num_2

# 2.Define a function max_of_three() that takes three numbers as arguments
# and returns the largest of them

def max_of_three(num_1, num_2, num_3):
    if num_1 > num_2:
        if num_1 > num_3:
            return num_1
        else:
            return num_2
    else:
        if num_2 > num_3:
            return num_2
        else:
            return num_3

# 3.Define a function that computes the length of a given list or string.
def mylen(string_or_list):
    count = 0
    for item in string_or_list:
        count += 1
    return count

# 4.Write a function that takes a character (i.e. a string of length 1)
# and returns True if it is a vowel, False otherwise.
def is_vowel(character):
    if character in 'aeiouAEIOU':
        return True
    else:
        return False

# 5.Write a function translate() that will translate a text into "rövarspråket"
# (Swedish for "robber's language"). That is, double every consonant
# and place an occurrence of "o" in between. For example,
# translate("this is fun") should return the string "tothohisos isos fofunon".
def translate(text):
    new_text = []
    new_character = ''
    for character in text:
        if character not in 'aeiouAEIOU' and character != ' ':
            new_character = character + 'o' + character
        else:
            new_character = character
        new_text.append(new_character)
    return ''.join(new_text)
print(translate("this is fun"))

# list -> str : ''.join(your_list)
# this joins every element in the list by a ''(empty character), and return this string

# str -> list :  your_str.split()



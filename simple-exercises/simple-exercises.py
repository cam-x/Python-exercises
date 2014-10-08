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
    for character in text:
        if character not in 'aeiouAEIOU' and character != ' ':
            new_character = character + 'o' + character
        else:
            new_character = character
        new_text.append(new_character)
    return ''.join(new_text)


# list -> str : ''.join(your_list)
# this joins every element in the list by a ''(empty character), and return this string

# str -> list :  your_str.split()

# 6.Define a function sum() and a function multiply() that sums and multiplies
# (respectively) all the numbers in a list of numbers. For example, sum([1, 2, 3, 4])
# should return 10, and multiply([1, 2, 3, 4]) should return 24.

def my_sum(numbers_list):
    mysum = 0
    for number in numbers_list:
        mysum += number
    return mysum


def multiply(numbers_list):
    mul = 1
    for number in numbers_list:
        mul *= number
    return mul


# 7. Define a function reverse() that computes the reversal of a string.
# For example, reverse("I am testing") should return the string "gnitset ma I".

def reverse(text):
    new_list = []
    for i in text[::-1]:
        new_list.append(i)
    return ''.join(new_list)


# 8.Define a function is_palindrome() that recognizes palindromes
# (i.e. words that look the same written backwards).
# For example, is_palindrome("radar") should return True.

def is_palindrome(text):
    return text == text[::-1]


# 9.Write a function is_member() that takes a value (i.e. a number, string, etc) x and a list of values a,
# and returns True if x is a member of a, False otherwise. (Note that this is exactly what the in operator does,
# but for the sake of the exercise you should pretend Python did not have this operator.)

def is_member(x, a):
    for i in a:
        if i == x:
            return True
    return False


# 10.Define a function overlapping() that takes two lists and returns True if
# they have at least one member in common,False otherwise.
# You may use your is_member() function, or the in operator,
# but for the sake of the exercise, you should (also) write it using two nested for-loops.

def overlapping(list_1, list_2):
    for i in list_1:
        for j in list_2:
            if i == j:
                return True
    return False


# 11.Define a function generate_n_chars() that takes an integer n and a character c and
# returns a string, n characters long, consisting only of c:s. For example,
# generate_n_chars(5,"x") should return the string "xxxxx".
# (Python is unusual in that you can actually write an expression 5 * "x" that will evaluate to "xxxxx".
# For the sake of the exercise you should ignore that the problem can be solved in this manner.)

def generate_n_chars(num, char):
    char_list = []
    for i in range(num):
        char_list.append(char)
    return ''.join(char_list)


# 12.Define a procedure histogram() that takes a list of integers and prints a histogram to the screen.
# For example, histogram([4, 9, 7]) should print the following:
# ****
# *********
# *******

def histogram(int_list):
    for i in int_list:
        print('*'*i)


# 13.The function max() from exercise 1) and the function max_of_three() from exercise 2)
# will only work for two and three numbers, respectively. But suppose we have a much larger number of numbers,
# or suppose we cannot tell in advance how many they are?
# Write a function max_in_list() that takes a list of numbers and returns the largest one.

def max_in_list(int_list):
    max_num = int_list[0]
    for i in int_list:
        if i > max_num:
            max_num = i
    return max_num

# 14.Write a program that maps a list of words
# into a list of integers representing the lengths of the corresponding words.

def word_map_length(word_list):
    int_list = []
    for word in word_list:
        int_list.append(len(word))
    return int_list


# 15.Write a function find_longest_word() that takes a list of words and returns the length of the longest one.

def find_longest_word(word_list):
    return max_in_list(word_map_length(word_list))


# 16.Write a function filter_long_words() that takes a list of words
# and an integer n and returns the list of words that are longer than n.

def filter_long_words(word_list, length):
    new_list = []
    for word in word_list:
        if len(word) > length:
            new_list.append(word)
    return new_list


# 17.Write a version of a palindrome recognizer that also accepts phrase palindromes
# Note that punctuation, capitalization, and spacing are usually ignored.

def palindrome(phrase):
    letter_list = []
    for char in phrase.lower():
        if char.isalpha():
            letter_list.append(char)
    return letter_list == letter_list[::-1]


# 18.A pangram is a sentence that contains all the letters of the English alphabet at least once,
# for example: The quick brown fox jumps over the lazy dog.
# Your task here is to write a function to check a sentence to see if it is a pangram or not.

def is_pangram(phrase):
    alpha_list = []
    for char in phrase.lower():
        if char.isalpha():
            alpha_list.append(char)
    if len(set(alpha_list)) == 26:
        return  True
    else:
        return  False

print(is_pangram("The quick brown f jumps over the lazy dog."))


# 19."99 Bottles of Beer" is a traditional song in the United States and Canada.
# It is popular to sing on long trips, as it has a very repetitive format which is easy to memorize,
# and can take a long time to sing. The song's simple lyrics are as follows:

def beer_song():
    for i in range(100, 0, -1):
        print("%d bottles of beer on the wall, %d bottles of beer" %(i, i))
        print("Take one down, pass it around, %d bottles of beer on the wall." %(i-1))
        print()
    return True


# 20.write a function translate() that takes a list of English words and returns a list of Swedish words.

def translate2(english_list):
    english_swedis = {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"år"}
    translate_list = []
    for english in english_list:
        if english in english_swedis:
           translate_list.append(english_swedis[english])
    return translate_list


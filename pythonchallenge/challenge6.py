import requests
import zipfile

__author__ = 'Jianqiao'
""" Get the file Zip from url
url = 'http://www.pythonchallenge.com/pc/def/channel.zip'
r = requests.get(url)
with open("channel.zip","wb") as code:  # 'w' - open for writing ; 'b' - binary mode
    code.write(r.content)
"""
my_zip = zipfile.ZipFile('channel.zip')  # class zipfile.ZipFile(file...) : Create a zipfile object
print(my_zip.namelist())
text = my_zip.read('readme.txt')    # Read the file which in the zipfile and return the bytes of that file.
print(text.decode())  # .decode() transform a byte data type into string.

number = '90052'
next_txt = number + '.txt'
comment_list = []
while True:
    try:
        text = my_zip.read(next_txt)
        #print(text.decode())
        comment_list.append(my_zip.getinfo(next_txt).comment.decode())  # Instances of the ZipInfo class are returned by
                                                                        # the getinfo() methods of ZipFile objects.
        number = text.decode().split()[-1]
        next_txt = number + '.txt'

    except :
        #print(text.decode(), 'you need to try manually', sep='\n') # sep= means separator.
        print('You should check the txt before this one'  )
        print('This is the comments:', ''.join(comment_list))
        my_zip.close()
        break



"""
import os
print(os.getcwdb())  # Get the directory you are working on
print(os.listdir())  # Get the list of all your directory name
os.remove('code3.zip') # Remove a file
"""

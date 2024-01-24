#Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt
import string
for i in string.ascii_uppercase:
    file_name = i + '.txt'
    # print (file_name)
    with open(file_name, 'w') as f:
        pass
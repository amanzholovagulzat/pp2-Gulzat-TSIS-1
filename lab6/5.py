#Write a Python program to write a list to a file.
mylist = ['My', 'Name', "is", "Aziz"]

with open("text.txt", "w") as f:
    for i in range(len(mylist)):
        f.write(mylist[i] + ' ')
#Write a Python program to check for access to a specified path. Test the existence, readability, writability and executability of the specified path
import os

path = 'lab1'
if os.path.exists(path):
    print("exist")
    if os.access(path, os.R_OK):
        print("readable")
    if os.access(path, os.W_OK):
        print("writable")
    if os.access(path, os.X_OK):
        print("executable")
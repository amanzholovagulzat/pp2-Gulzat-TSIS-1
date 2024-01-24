#Write a Python program to test whether a given path exists or not. If the path exist find the filename and directory portion of the given path.
import os

path = 'C:\Users\Алуа\Desktop\PP2'
if os.path.exists(path):
    print( os.path.basename(path) )
    print( os.path.dirname(path) )
else:
    print( 'not exist' )
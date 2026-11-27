'''
wie kann python auf den Namen der eigenen Datei zugreifen, etc.
Created on 16.11.2026

https://www.geeksforgeeks.org/python/find-path-to-the-given-file-using-python/

https://docs.python.org/3/library/os.path.html


@author: Fritz Lindhauer
'''

import os

print('File name :    ', os.path.basename(__file__))
print('Directory Name:     ', os.path.dirname(__file__))
print('absPath():      ', os.path.abspath(__file__))

# -*- coding: utf-8 -*-

'''
Auszug aus dem Buch: "Definitive Guide to Jython"

Created on 02.11.2026

Pickle
One of the most popular modules in the Python language is the pickle module. 
The goal of this module is basically to allow for the serialization and persistence of Python objects to disk in file format. 
A pickled object can be written to disk using this module, and it can also be read back in and utilized in object format. 
Just about any Python object can be persisted using pickle.

To write an object to disk, we call the pickle() function. 
The object will be written to file in a format that may be unusable by anything else, 
but we can then read that file back into our program and use the object as it was prior to writing it out. 
In the following example, we’ll create a Player object and then persist it to file using pickle. 
Later, we will read it back into a program and make use of it. 
We will make use of the file object when working with the pickle module.

@author: Fritz Lindhauer
'''

TODOGOON20261102


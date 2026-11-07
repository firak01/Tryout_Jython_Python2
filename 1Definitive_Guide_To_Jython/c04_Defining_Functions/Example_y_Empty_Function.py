# -*- coding: utf-8 -*-

'''
Auszug aus dem Buch: "Definitive Guide to Jython"

Created on 02.11.2026

@author: Fritz Lindhauer
'''

def do_nothing():
    pass # here's how to specify an empty body of code


def empty_callback(*args, **kwargs):
    """Use this function where we need to supply a callback,
       but have nothing further to do.
    """
    
do_nothing()

empty_callback()

print "Hier gibt es nix zu sehen"
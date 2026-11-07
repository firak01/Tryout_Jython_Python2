# -*- coding: utf-8 -*-

'''
Auszug aus dem Buch: "Definitive Guide to Jython"

Created on 02.11.2026

@author: Fritz Lindhauer
'''

# Define a function that takes two values and a mathematical function
def perform_calc(value1, value2, func):
     return func(value1, value2)
 
# Define a mathematical functions to pass
def mult_values(value1, value2):
     return value1 * value2

def add_values(value1, value2):
    return value1 + value2
 
# Führe nun die erste Funktion aus und übergib die gewünschte Methode:
result = perform_calc(2,4, mult_values)
print "resultA %s" % result

result = perform_calc(2,4, add_values)
print "resultB %s" % result






 
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

def times_by(n, by=2):
    return n * by
 
# Führe nun die erste Funktion aus und übergib die gewünschte Methode:
result = perform_calc(2,4, times_by)
print "resultA %s" % result

# ABER: DAS GEHT NICHT, DA 3 ARGUMENTE ERWARTET WERDEN
# result = perform_calc(2,times_by)


print "resultB %s" % result








 
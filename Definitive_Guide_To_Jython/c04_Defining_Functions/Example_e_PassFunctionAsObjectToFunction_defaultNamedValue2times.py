# -*- coding: utf-8 -*-

'''
Auszug aus dem Buch: "Definitive Guide to Jython"

Created on 02.11.2026

@author: Fritz Lindhauer
'''

# Define a function that takes two values and a mathematical function
# Hier wird der 2te Wert mit default belegt. WICHTIG: DEFAULT WERTE IMMER AM SCHLUSS
# Merke: Ich mache hier einen anderen Defaultwert für value2 als in der times_by Funktion!!!
def perform_calc2(value1, func, value2=3):
     return func(value1, value2)

 
# ------------------------------------------------------
# Define a mathematical functions to pass
def mult_values(value1, value2):
     return value1 * value2

def add_values(value1, value2):
    return value1 + value2

def times_by(n, by=2):
    return n * by
 
# Führe nun die erste Funktion aus und übergib die gewünschte Methode:
result = perform_calc2(2, times_by, 4)
print "resultA ohne Defaultwert: %s" % result

# ABER: DAS GEHT OHNE DEFAULTWERT NICHT, DA 3 ARGUMENTE ERWARTET WERDEN
# result = perform_calc2(2,times_by)

# Geht das nun, mit dem 2ten Wert oben als Default? JA
result = perform_calc2(2, times_by)
print "resultB mit Defaultwert: %s" % result










 
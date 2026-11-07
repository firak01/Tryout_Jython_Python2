# -*- coding: utf-8 -*-

'''
Auszug aus dem Buch: "Definitive Guide to Jython"

Rekursion
und meine Experimente mit der Funktionsübergabe und dem Defaultwert. 


Ausserdem wird hier der Aufbau der Hilfe-Dokumentation erklärt:
3 Hochkomma am Anfang des Funktionsblocks
...
Any such docstring, but with leading indentation stripped, becomes the __doc__ attribute of that function object. 
Incidentally, docstrings are also used for modules and classes, and they work exactly the same way.

You can now use the help built-in function to get the docstring, 
or see them from various IDEs like PyDev for Eclipse and nbPython for NetBeans as part of the auto-complete.
..

Created on 02.11.2026

@author: Fritz Lindhauer
'''

# Definiere hier die Berechnungsfunktion mit nur 1 Argument. 
# Das ziel ist, das damit die Defaultwerte der Mathematischen Funktion "verwendet werden".
# ABER: Mit dem gleichen Namen geht das nicht...
def perform_calc1(func, value1=2):
     return func(value1)

#############
# Mathematische Funktion
# Fakultät, 
# ausserdem wird hier im Beispiel gezeigt, wo die Dokumentationsfunktion stehen soll. 
# 3x Hochkomma als erste Einträge in der Funktion. Diese werden zum __doc__ Attribut, auswertbar für die help(...) Funktion.
def fact(n):
    """Returns the factorial of n

    Computes the factorial of n recursively. Does not check its
    arguments if nonnegative integer or if would stack
    overflow. Use with care!
    """
    
    if n in (0, 1):
        return 1
    else:
        return n * fact(n - 1)
    
###########   
# Aufruf der Hilfefunktion, die dann den Text in den 3 Hochkommata anzeigen soll
help(fact)


########### 
x=3 # 3*2*1
result = perform_calc1(fact, x)
print "result der Argumente mit fact-Function: %s" % result

result = perform_calc1(fact) # 2*1
print "result der Argumente mit fact-Function mit Default: %s" % result
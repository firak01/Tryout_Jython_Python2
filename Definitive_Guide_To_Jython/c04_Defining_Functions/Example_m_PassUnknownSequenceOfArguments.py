# -*- coding: utf-8 -*-

'''
Auszug aus dem Buch: "Definitive Guide to Jython"

Lastly, a function can take an unspecified number of ordered arguments, through *args, and keyword args, through **kwargs. 
These parameter names (args and kwargs) are conventional, so you can use whatever name makes sense for your function. 
The markers * and ** are used to to determine that this functionality should be used. 
The single * argument allows for passing a sequence of values, 
and a double ** argument allows for passing a dictionary of names and values. 
If either of these types of argument is specified, they must follow any single arguments in the function declaration. 
Furthermore, the double ** must follow the single *.

Created on 02.11.2026

@author: Fritz Lindhauer
'''

# Definiere hier die Berechnungsfunktion mit nur 1 Argument. 
# Das ziel ist, das damit die Defaultwerte der Mathematischen Funktion "verwendet werden".
# ABER: Mit dem gleichen Namen geht das nicht...
def perform_calc1(value1, func):
     return func(value1)
 
def perform_calc1seq(func, *value1):
    
    # Wichtig: *value1 wird in Einzelwerte entpackt.
    # Aber, da wir in sum_args wieder eine gepacktes Tuple erwarten, müssen wir es mit * erneut packen.
    # Also bei: return func(value1)
    #           TypeError: unsupported operand type(s) for +: 'int' and 'tuple' 
     return func(*value1)
 

#####################################################
# Define a mathematical functions to pass
def sum_args(*nums):
 
    # Setzt man nun wieder ein * davor, werden die Einzelwerte wieder in ein Tuple gepackt.
    # Fehlermelung wäre dann:
    # TypeError: sum() takes 1-2 arguments (4 given)  
    # Also diesmal die entpackten Einzewerte belassen
    return sum(nums)


####################################################
seq = [6,5,4,3]

# wichtig, zum Zusammenpacken der Einzelwerte hier schon * setzen
result = sum_args(*seq)
print "result der Argumente: %s" % result

# wichtig, zum Zusammenpacken der Einzelwerte hier schon * setzen
result = perform_calc1seq(sum_args, *seq)
print "result der Argumente mit sum-Function: %s" % result







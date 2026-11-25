# -*- coding: utf-8 -*-
'''
Created on 31.10.2026

@author: Fritz Lindhauer


Auszug aus dem Buch: "Definitive Guide to Jython"


Using def for define seems simple enough, 
and this keyword certainly can be used to declare a function just like you would in a static language. 
You should write most code that way in fact.

However, a function definition can occur at any level in your code 
and be introduced at any time. 
Unlike the case in a language like C or Java, function definitions are not declarations. 
Instead they are executable statements. You can nest functions, and we’ll describe that more when we talk about nested scopes. 
And you can do things like conditionally define them.

This means it’s perfectly valid to write code like the following:
'''


'''
Bemerkenswert:
Dieser Code läuft nur, wenn in einer der ersten beiden Zeilen des Scripts die Kodierungsanweisung steht.

# -*- coding: utf-8 -*-
'''
variant=True
sy='zwei'

if variant:
    def f(sx):
       # Python2 Syntax, da wir hier Jython 2.7 haben 
       print "One way:  %s" % sx
       # Python3 wäre so print("One way:  %s" % sx)
       return
       
else:
    def f(sx):
       # Python 2 Syntax, da wir hier Jython 2.7 haben
       print "or another:  %s" % sx
       # Python 3 wäre so print("or another:  %s" % sx)
       return

# Aufruf der dynamsch definierten Funktionen (das ist in Java so nicht möglich)
# Wichtig: Diese Zeile muss hinter der Funktionsdefinition stehen.
#          Das ist in Java nicht nötig, da die Methoden dekaliert werden.
f(sy)
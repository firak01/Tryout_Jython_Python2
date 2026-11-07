# -*- coding: utf-8 -*-

'''
Auszug aus dem Buch: "Definitive Guide to Jython"

Created on 02.11.2026

@author: Fritz Lindhauer
'''

print "Variante 1) Enter your favourite team"

# Obtain a value from the command line and store it into a variable
import sys
fav_team = sys.stdin.readline()
sys.stdout.write("Variante 1) My favorite team is: %s" % fav_team)

# Obtain a value using raw_input and store it into a variable
fav_team = raw_input("Variante 2) Enter your favorite team: ")
sys.stdout.write("Variante 2) My favorite team is: %s" % fav_team)


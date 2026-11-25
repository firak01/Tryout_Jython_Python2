# -*- coding: utf-8 -*-

'''
Auszug aus dem Buch: "Definitive Guide to Jython"
Merke: In Kapitel 5 werden einfache Werte von der Kommandozeile gelesen.

Created on 25.11.2026

@author: Fritz Lindhauer
'''

from optparse import OptionParser, Option

print "Argumente -f --foo"
print "Argumente -b --bar"

# Obtain a value from the command line 
parser = OptionParser()
parser.add_option("-f", "--foo", help="set foo option")
parser.add_option("-b", "--bar", help="set bar option")

# mache hier wohl ein dictionary
(options, args) = parser.parse_args()
print "options: %s" % Option
print "args: %s" % args



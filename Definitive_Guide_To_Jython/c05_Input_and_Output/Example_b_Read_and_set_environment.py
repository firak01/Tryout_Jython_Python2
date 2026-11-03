# -*- coding: utf-8 -*-

'''
Auszug aus dem Buch: "Definitive Guide to Jython"

Created on 02.11.2026

@author: Fritz Lindhauer
'''

import os

print "Liste alle Umgebungsvariablen"
# Übernimm die Liste in ein (Python Sprech) "Dictionary"
dictionaryOs = os.environ
# !!! NICHT WEITERGEBEN. HIER IST DER API KEY DRIN... 
print dictionaryOs


# Gezielt eine Variable ansprechen
# os.environ["HOME"] Da es in der Entwicklungsumgebung kein HOME gibt, wird ein KeyError:'HOME' geworfen

# Change/Set home directory for the Python session
os.environ["HOME"] = "/newhome"
newHomePath = os.environ["HOME"]
print "neuer Homepath '%s'" % newHomePath

#Gibt es laut dem Dictionary Print
#ACHTUNG: environ ist keine Methode.... darum geht das nicht in runden Klammern   os.environ("CLIENTNAME")
clientName = os.environ["CLIENTNAME"]
print "Clientname '%s'" % clientName

#Man kann auch per Funktion arbeiten
pythonPath = os.environ.get("PYDEV_COMPLETER_PYTHONPATH")
print "Pythonpath '%s'" % pythonPath


 




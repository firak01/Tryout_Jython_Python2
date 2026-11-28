# -*- coding: utf-8 -*-

'''
Weiterentwicklung von tryoutString01ZZZ

Hier werden die notwendigen Pfade dürch den JavaClasspathLoaderZZZ.py
aus einer durch Maven im Eclipse Projekt erstellten Textdatei ausgelesen.
Die so ausgelesenen .jar Bibliotheken verden dem Pythonpath hinzugefügt.

Erweitert wird hier die Verwendung des JythonKerneJYZ Objekts, 
mit dem vorweg noch die Projekt noch ausgewählt werden können, welche man einbinden möchte.

Created on 04.11.2026

@author: Fritz Lindhauer
'''

# Classpath programmatisch konfigurieren
# Die kurze Form unten reicht, da in __init__.py des entsprechenden Pakets der JavaClasspathLoaderZZZ "nach aussen kommuniziert" wird.
# Alternativ müsste man die Klasse direkt importieren
# from jyz.basic.jython.jazkernel.JythonKernelJYZ import JythonKernelJYZ
from jyz.basic.jython.jazkernel import *
oJythonKernel = JythonKernelJYZ()
#20261128: Man braucht den Projketnamen nicht mehr redundant übergeben
#oJythonKernel.addProject('JAZKernelEngine', 'Projekt_Kernel02_JAZKernelEngine\JAZKernelEngine')
oJythonKernel.addProject('JAZKernelEngine', 'Projekt_Kernel02_JAZKernelEngine')
oJythonKernel.loadProjectPaths()


# Erst jetzt Java-Klassen importieren
from java.lang import System
from basic.zBasic.util.datatype.string import StringZZZ

print("Java-Version:")
print(System.getProperty("java.version"))

print("Aktueller Zeitstempel:")
print(System.currentTimeMillis())

qString='das ist toll'
result = StringZZZ.capitalize(qString)
print(result)

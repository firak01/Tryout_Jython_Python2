# -*- coding: utf-8 -*-

'''
Weiterentwicklung von tryoutString01ZZZ

Hier werden die notwendigen Pfade dürch den JavaClasspathLoaderZZZ.py
aus einer durch Maven im Eclipse Projekt erstellten Textdatei ausgelesen.
Die so ausgelesenen .jar Bibliotheken verden dem Pythonpath hinzugefügt.

Created on 04.11.2026

@author: Fritz Lindhauer
'''

# Classpath konfigurieren
# Das reicht, da in __init__.py der JythonKernelZZZ "nach aussen kommuniziert" wird.
from basic.jython.jazkernel import *
oJythonKernel = JythonKernelZZZ()
oJythonKernel.addProject('JAZKernelEngine', 'Projekt_Kernel02_JAZKernelEngine\JAZKernelEngine')
oJythonKernel.loadProjectPaths()


# Erst jetzt Java-Klassen importieren
from java.lang import System
from basic.zBasic.util.system import SystemSingletonZZZ
from basic.zBasic.util.system import IPrintLevelUserZZZ
from basic.zBasic.util.datatype.string import StringZZZ
from custom.zKernel import Log


print("Java-Version:")
print(System.getProperty("java.version"))

print("Aktueller Zeitstempel:")
print(System.currentTimeMillis())

qString='das ist toll'
result = StringZZZ.capitalize(qString)
print(result)

# Ein Enum zu übergeben habe ich nicht geschafft. Der String ist der Workaround.
qLevel='DEBUG'

# Am Enum liegr der "Argumentanzahl" Fehler nicht. Sondern daran, das man die Schritte einzeln machen muss, also statt
# SystemSingletonZZZ.getInstance().setPrintLevelOverall(qLevel)
# Muss man erst eine Instanz holen und zuweisen. 
a = SystemSingletonZZZ.getInstance()
a.setPrintLevelOverall(qLevel) 

# Das Enum ist doch übergebebar. Hauptsache oben import definiert und die Instanz des Objekts vorhanden. 
a.setPrintLevelOverall(IPrintLevelUserZZZ.PRINTLEVEL.DEBUG)

# Bei eingestelltem Debug level wird dies 2x ausgegeben. Einmal als einfacher String, Davor aber als Consolen-Text-Formatiert String
Log.writeInfo("ach ein Log, endlich")

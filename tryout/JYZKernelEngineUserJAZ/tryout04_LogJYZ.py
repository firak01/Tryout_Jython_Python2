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

# Ein Enum zu übergeben htte ich zunächst nicht geschafft. Der String war dann funktionierende Workaround.
# Mit einem geringeren Debug-Level wird auch weniger ausgegeben
#qLevel='INFO'
#qLevel='DEBUG'

# Muss man erst eine Instanz holen und zuweisen. 
#systemZZZ = SystemSingletonZZZ.getInstance()
#systemZZZ.setPrintLevelOverall(qLevel) 

# ------------------------------------------------------------------------------------------------------------------------
# Hier mit Übergabe eines Enums:
# Am Enum lieg der "Argumentanzahl" Fehler nicht. Sondern daran, das man die Schritte einzeln machen muss, also statt
# SystemSingletonZZZ.getInstance().setPrintLevelOverall(qLevel)
# Muss man erst eine Instanz holen und zuweisen. 
systemZZZ = SystemSingletonZZZ.getInstance()


# Das Enum ist doch übergebar. Hauptsache oben import definiert und die Instanz des Objekts vorhanden.
# Ausserdem wieder nicht versuchen alles in eine String zu schreiben.
# Also nicht, IPrintLevelUserZZZ.PRINTLEVEL.DEBUG , sondern:
enumPrintLevel = IPrintLevelUserZZZ.PRINTLEVEL

# Mit einem geringeren Debug-Level wird auch weniger ausgegeben. 
#systemZZZ.setPrintLevelOverall(enumPrintLevel.INFO)
systemZZZ.setPrintLevelOverall(enumPrintLevel.DEBUG)

# Merke: Bei eingestelltem Debug level wird dies 2x ausgegeben. Einmal als einfacher String, Davor aber als Consolen-Text-Formatiert String
Log.writeInfo("ach ein Log, endlich")

# -------------------------------------------------------------------------------------------------------------------------
# Noch einmal StringZZZ aufrufen, als positives Ergebnis ;-)
qString='das ist toll'
result = StringZZZ.capitalize(qString)
print(result)

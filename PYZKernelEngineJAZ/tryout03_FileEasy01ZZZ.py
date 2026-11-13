# -*- coding: utf-8 -*-

'''
Weiterentwicklung von tryout02_FileEasy01ZZZ

Nun wird das FileEasyZZZ-Objekt mit seinen static Methoden genutzt.

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
from basic.zBasic.util.file import FileEasyZZZ

print("Java-Version:")
print(System.getProperty("java.version"))

print("Aktueller Zeitstempel:")
print(System.currentTimeMillis())

result = FileEasyZZZ.getDirectoryOfExecutionAsString()
print(result)

# -*- coding: utf-8 -*-

'''
Weiterentwicklung von tryoutString01ZZZ

Hier werden die notwendigen Pfade dürch den JavaClasspathLoaderZZZ.py
aus einer durch Maven im Eclipse Projekt erstellten Textdatei ausgelesen.
Die so ausgelesenen .jar Bibliotheken verden dem Pythonpath hinzugefügt.

Created on 04.11.2026

@author: Fritz Lindhauer
'''
from JavaClasspathLoaderZZZ import JavaClasspathLoaderZZZ

# Classpath konfigurieren
oLoader = JavaClasspathLoaderZZZ()

print("Basisverzeichnis:")
print(oLoader.getBasePath())

# Java-Projekt einbinden
oLoader.addPath(
    r"..\..\Projekt_Kernel02_JAZKernelEngine\JAZKernelEngine\target\classes"
)

# Maven-Abhängigkeiten des Projekts einbinden
oLoader.addClasspathFile(
    r"..\..\Projekt_Kernel02_JAZKernelEngine\JAZKernelEngine\target\classpathZZZ\classpathByMavenZZZ.txt"
)

# Sonstige Externe Bibliotheksabhängigkeiten des Projekts einbinden,
# alternativ zum Einbinden in vmargs bei der Launch Konfiguration, wie:
# -Dpython.path=C:\1fgl\workspace\EclipseOxygen_V02\ZKernelFileCollection\commons-lang-2.1.jar
oLoader.addClasspathFile(
    r"..\..\Projekt_Kernel02_JAZKernelEngine\JAZKernelEngine\target\classpathZZZ\classpathOfLibrariesExternalZZZ.txt"
)


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

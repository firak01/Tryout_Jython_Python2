# -*- coding: utf-8 -*-

'''
Weiterentwicklung von tryoutString02ZZZ

Nun wird das FileEasyZZZ-Objekt mit seinen static Methoden genutzt.

Hier werden die notwendigen Pfade dürch den JavaClasspathLoaderZZZ.py
aus einer durch Maven im Eclipse Projekt erstellten Textdatei ausgelesen.
Die so ausgelesenen .jar Bibliotheken verden dem Pythonpath hinzugefügt.

Zur Erstellung der Maven-Textdatei, s. in den Java Projekten der Ordner buildZZZ.

Created on 04.11.2026

@author: Fritz Lindhauer
'''

# Umgebungsvariablen auslesen, insbesondere die, die beim EclipseStart per Batch gesetzt werden
import os
sWorkspace = os.environ.get("MY_DATA")

if not sWorkspace:
    raise Exception("Umgebungsvariable MY_DATA nicht gesetzt!")

print("Eclipse Workspace Verzeichnis:")
print(sWorkspace)

# Classpath programmatisch konfigurieren
# Die kurze Form unten reicht, da in __init__.py des entsprechenden Pakets der JavaClasspathLoaderZZZ "nach aussen kommuniziert" wird.
# Alternativ müsste man die Klasse direkt importieren
# from jyz.basic.jython.jazkernel.JavaClasspathLoaderJYZ import JavaClasspathLoaderJYZ
from jyz.basic.jython.jazkernel import JavaClasspathLoaderJYZ
oLoader = JavaClasspathLoaderJYZ()

print("Basisverzeichnis (Repository-Verzeichnis):")
print(oLoader.getBasePath())

# Java-Projekt einbinden
oLoader.addPath(
    r"Projekt_Kernel02_JAZKernelEngine\JAZKernelEngine\target\classes"
)

# ZKernelFileCollection Bibliotheksabhängigkeiten des Projekts einbinden.
# Diese sind relativ zum Eclipse Workspace angegeben. Dieser Pfad wird über meine Batch beim Eclipsestart gesetzt.
# Mehrere Pfade werden mit Semikolon getrennt.
# Z.B.: \ZKernelFileCollection\commons-lang-2.1.jar
#
# Wichtig: zusätzliche Argument sWorkspace am Ende
oLoader.addClasspathFile(
    r"Projekt_Kernel02_JAZKernelEngine\JAZKernelEngine\target\classpathZZZ\classpathOfLibrariesWorkspaceZZZ.txt", sWorkspace
)

# Maven-Abhängigkeiten des Projekts einbinden.
# Diese sind als absoluter Pfad angegeben, mehrere Pfade mit Semikolon getrennt.
oLoader.addClasspathFile(
    r"Projekt_Kernel02_JAZKernelEngine\JAZKernelEngine\target\classpathZZZ\classpathOfLibrariesByMavenZZZ.txt"
)

# Sonstige Externe Bibliotheksabhängigkeiten des Projekts einbinden.
# Diese sind als absoluter Pfad angegeben, mehrere Pfade mit Semikolon getrennt.
# alternativ zum Einbinden in vmargs bei der Launch Konfiguration, wie:
# -Dpython.path=C:\1fgl\workspace\EclipseOxygen_V02\ZKernelFileCollection\commons-lang-2.1.jar
oLoader.addClasspathFile(
    r"Projekt_Kernel02_JAZKernelEngine\JAZKernelEngine\target\classpathZZZ\classpathOfLibrariesExternalZZZ.txt"
)

# Erst jetzt Java-Klassen importieren
from java.lang import System
from basic.zBasic.util.file import FileEasyZZZ

print("Java-Version:")
print(System.getProperty("java.version"))

print("Aktueller Zeitstempel:")
print(System.currentTimeMillis())

result = FileEasyZZZ.getDirectoryOfExecutionAsString()
print(result)

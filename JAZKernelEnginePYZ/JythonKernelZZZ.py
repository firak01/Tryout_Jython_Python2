# -*- coding: utf-8 -*-

'''

Klasse für die Initialisierung von Jython für die Zusammenarbeit mit den ZKernel-Projekten
- lade die notwendigen Java-Bibliotheken der Projekte


Created on 06.11.2026

@author: Fritz Lindhauer
'''

import os
import sys
from test.test_re import todo_on_jython
from tryout01_String02ZZZ import sWorkspace

class JythonKernelZZZ(object):
    
    def __init__(self):
        # Umgebungsvariablen auslesen, insbesondere die, die beim EclipseStart per Batch gesetzt werden
        # import os
        sWorkspace = os.environ.get("MY_DATA")
        
        if not sWorkspace:
            raise Exception("Umgebungsvariable MY_DATA nicht gesetzt!")
        
        print("Eclipse Workspace Verzeichnis:")
        print(sWorkspace)
        
        # Classpath konfigurieren
        from JavaClasspathLoaderZZZ import JavaClasspathLoaderZZZ
        oLoader = JavaClasspathLoaderZZZ()
        
        print("Basisverzeichnis (Repository-Verzeichnis):")
        print(oLoader.getBasePath())
        
    def addProject(self, sProjectName, sProjectPath):
        TODOGOON #fülle hier das dictionary mit den notwendigen Projekten        
        return True
        
    def getProjectPathForProject(self, sProjectName):
        TODOGOON #lies den Eintrag aus dem dictionary und fülle sProjectPath
        sProjectPath = "Name aus dem dictionary ausgelesen"
        return sProjectPath
    
    def loadProjectPaths(self):
        TODOGOON # arbeite die Enträge aus dem dictionary ab
                 # in einer Schleife aufrufen loadProjectPath(sProjectname)
        return True
        
    
    def loadProjectPath(self, sProjectName):
        import os
        sWorkspace = os.environ.get("MY_DATA")

        if not sWorkspace:
            raise Exception("Umgebungsvariable MY_DATA nicht gesetzt!")

        
        #########################################################
        # holen aus dem Dictionary für den sProjectName den definierten sPrjectPath
        sProjectPath = self.getProjectPathForProject(sProjectName)
        
        # Java-Projekt einbinden
        # Beispiel:   r"..\..\Projekt_Kernel02_JAZKernelEngine\JAZKernelEngine\target\classes"
        sProjectPath4Java = r"'..\..\' sProjectPath '\target\classes'"
        self.oLoader.addPath(sProjectPath4Java)
        
        # ZKernelFileCollection Bibliotheksabhängigkeiten des Projekts einbinden.
        # Diese sind relativ zum Eclipse Workspace angegeben. Dieser Pfad wird über meine Batch beim Eclipsestart gesetzt.
        # Mehrere Pfade werden mit Semikolon getrennt.
        # Z.B.: \ZKernelFileCollection\commons-lang-2.1.jar
        #
        # Wichtig: zusätzliche Argument sWorkspace am Ende
        # Beispiel: r"..\..\Projekt_Kernel02_JAZKernelEngine\JAZKernelEngine\target\classpathZZZ\classpathOfLibrariesWorkspaceZZZ.txt", sWorkspace
        sProjectPath4Workspace = r"'..\..\' sProjectPath '\target\classpathZZZ\classpathOfLibrariesWorkspaceZZZ.txt'"       
        self.oLoader.addClasspathFile(sProjectPath4Workspace, sWorkspace)
        
        # Maven-Abhängigkeiten des Projekts einbinden.
        # Diese sind als absoluter Pfad angegeben, mehrere Pfade mit Semikolon getrennt.
        # Beispiel: r"..\..\Projekt_Kernel02_JAZKernelEngine\JAZKernelEngine\target\classpathZZZ\classpathOfLibrariesByMavenZZZ.txt"
        sProjectPath4Maven = r"'..\..\' sProjectPath 'target\classpathZZZ\classpathOfLibrariesByMavenZZZ.txt'"
        self.oLoader.addClasspathFile(sProjectPath4Maven)
        
        # Sonstige Externe Bibliotheksabhängigkeiten des Projekts einbinden.
        # Diese sind als absoluter Pfad angegeben, mehrere Pfade mit Semikolon getrennt.
        # alternativ zum Einbinden in vmargs bei der Launch Konfiguration, wie:
        # -Dpython.path=C:\1fgl\workspace\EclipseOxygen_V02\ZKernelFileCollection\commons-lang-2.1.jar
        # Beispiel: r"..\..\Projekt_Kernel02_JAZKernelEngine\JAZKernelEngine\target\classpathZZZ\classpathOfLibrariesExternalZZZ.txt"
        sProjectPath4External = r"'..\..\' sProjectPath 'target\classpathZZZ\classpathOfLibrariesExternalZZZ.txt'"
        self.oLoader.addClasspathFile(sProjectPath4External)   
        
        
        
        
                

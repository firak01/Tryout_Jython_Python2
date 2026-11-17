# -*- coding: utf-8 -*-

'''
Klasse für die Initialisierung von Jython für die Zusammenarbeit mit den ZKernel-Eclipse-Projekten
- lade die notwendigen Java-Bibliotheken der Projekte / Initializes Jython's Java classpath for one or more Eclipse projects.


Created on 06.11.2026

@author: Fritz Lindhauer
'''


import os
from basic.jyzBasic.reflection import *
from basic.jyzBasic.util.abstractArray import *
from basic.jyzBasic.util.datatype.string import *

# Cool man kann auch einzelen Variablen importieren
# Aber klaptt wohl nur im gleichen Sourcepath, nicht hier im tryout-Path 
#from basic.zBasic.reflection.tryout01_ReflectCode01ZZZ import sFilePathTotal
#from basic.zBasic.reflection.tryout01_ReflectCode01ZZZ import sProjectPath


class JythonKernelJYZ(object):

    def __init__(self, sWorkspace=None, oLoader=None):
        # MY_DATA is the Eclipse workspace root used by the generated
        # workspace-relative classpath files.
        self.sWorkspace = sWorkspace or os.environ.get("MY_DATA")
        if not self.sWorkspace:
            raise Exception("Umgebungsvariable MY_DATA nicht gesetzt!")
        self.sWorkspace = os.path.abspath(self.sWorkspace)

        from JavaClasspathLoaderJYZ import JavaClasspathLoaderJYZ
        self.oLoader = oLoader or JavaClasspathLoaderJYZ()
        self.dProject = {}

        print("Eclipse Workspace Verzeichnis:")
        print(self.sWorkspace)
        print("Basisverzeichnis (Repository-Verzeichnis):")
        print(self.oLoader.getBasePath())

    def addProject(self, sProjectName, sProjectPath):
        """Register a project path relative to MY_DATA / relative to the current code directory (or an absolute path)."""
        if not sProjectName:
            raise ValueError("Projektname darf nicht leer sein!")
        if not sProjectPath:
            raise ValueError("Projektpfad darf nicht leer sein!")
        self.dProject[sProjectName] = sProjectPath
        return True

    def getProjectPathForProject(self, sProjectName):
        if sProjectName not in self.dProject:
            raise KeyError("Projekt nicht registriert: " + str(sProjectName))
        sProjectPath = self.dProject[sProjectName]
        if not os.path.isabs(sProjectPath):
            # TODOGOON20261115 #Ermittle die Anzahl der zurückzugehenden Verzeichnisse automatisch
            '''           
            Erst aus dem Projekt zurück zum Root (Das ist der Root des Repositories)
            Wichtig: Ausgangslage ist das Verzeichnis, in dem die .py Datei liegt, in welcher über den Code die Java klassen importiert werden sollen, Z.B.
                              
                # Classpath konfigurieren
                # Das reicht, da in __init__.py der JythonKernelZZZ "nach aussen kommuniziert" wird.
                from basic.jython.jazkernel import *
                oJythonKernel = JythonKernelZZZ()
                oJythonKernel.addProject('JAZKernelEngine', 'Projekt_Kernel02_JAZKernelEngine\JAZKernelEngine')
                oJythonKernel.loadProjectPaths()
              
            
            
            Also, die .py Datei liegt hier:
                C:\1fgl\repo\EclipseOxygen_V02\Tryout_Jython_Python2\tryout\PYZKernelEngineJAZ\tryout04_LogZZZ.py
                Das sind 3 Ebenen bis zm Eclipse "repository Base" Verzeichnis
                Demnach 3 mal in os.path.join: "..",
                
                
            Mache ähnliches ins JavaClasspathLoader.py:
            
                def getBasePathOffset(self):
                    # TODOGOON20261109 depth ausrechnen
                    depth=5
                    return depth

            '''
            
            # Woher kommt der RepoBasis-Pfad?
            sProjectPathRepo = r"C:\1fgl\repo\EclipseOxygen_V02\Tryout_Jython_Python2"
            # sFilePathTotal  =  r"C:\1fgl\repo\EclipseOxygen_V02\Tryout_Jython_Python2\tryout\PYZKernelEngineJAZ\tryout04_LogZZZ.py"
           
            # Nein, es ist nicht der Pfad der Datei, die den import macht, sondern
            # Der Pfad zu dieser Datei, in der wir gerade sind:
            #sFilePathTotal = r"C:\1fgl\repo\EclipseOxygen_V02\Tryout_Jython_Python2\src\basic\jython\jazkernel\JythonKernelZZZ.py"
            
                      
            print("----- Pfadvergleich: Pfad zur eigenen Datei -----")
            print("errechneter Pfad:")
            print('File name :         ', os.path.basename(__file__))
            print('Directory Name:     ', os.path.dirname(__file__))
            print('abspath(__file__):  ', os.path.abspath(__file__))
            
            print("statischer Pfad:")
            print('Variante a:         ', r"C:\HIS-Workspace\1fgl\repo\EclipseOxygen_V02\Tryout_Jython_Python2\tryout\PYZKernelEngineJAZ\tryout04_LogZZZ.py")
            print('Variante b:         ', r"C:\HIS-Workspace\1fgl\repo\EclipseOxygen_V02\Tryout_Jython_Python2\src\basic\jython\jazkernel\JythonKernelZZZ.py")
            
          
            
            print("----- Pfadvergleich: Pfad zum Repository Verzeichnis -----")
            print("errechneter Pfad:")            
            print('os.getenv("sRLZZZ"):  ', os.getenv("sRLZZZ") )           
            print("statischer Pfad:")
            print('Variante a:           ', r"C:\HIS-Workspace\1fgl\repo\EclipseOxygen\Tryout_Jython_Python2")            
            
            
          
            #iPackageDepth = ReflectCodeZZZ.computePackageDepth(sFilePathTotal, sProjectPath)
            #print "Pakettiefe: %s" %iPackageDepth
                  
            sProjectPathRepo = os.getenv("sRLZZZ")
            sFilePathTotal = os.path.abspath(__file__)
            iWorkspaceDepth = ReflectCodeJYZ.computWorkspaceDepth(sFilePathTotal, sProjectPathRepo)
            print "Workspacetiefe immer um 1 erhöht: %s" %iWorkspaceDepth
            
            saPathOffset = ArrayUtilJYZ.createArray("..", iWorkspaceDepth)
            sPackageDepth = StringArrayJYZ.implode(saPathOffset, "\\")

            #sProjectPath = os.path.join("..","..", sProjectPath) 
            sProjectPath = os.path.join(sPackageDepth, sProjectPath)
            
        #Merke: Das entfernt redundante Pfadbestandteile und .. also nicht: return os.path.abspath(sProjectPath)
        return sProjectPath

    def loadProjectPaths(self):
        iCount = 0
        for sProjectName in self.dProject:
            if self.loadProjectPath(sProjectName):
                iCount += 1
        return iCount

    def loadProjectPath(self, sProjectName):
         # holen aus dem Dictionary für den sProjectName den definierten sPrjectPath
        sProjectPath = self.getProjectPathForProject(sProjectName)
        
        #sProjectPath = os.path.join("..", "..", sProjectPath) 
        
        # Load compiled project classes and the three generated dependency lists.
        
        # 1) Java-Projekt einbinden
        # Beispiel:   r"..\..\Projekt_Kernel02_JAZKernelEngine\JAZKernelEngine\target\classes"      
        sClasses = os.path.join(sProjectPath, "target", "classes")
        self.oLoader.addPath(sClasses)

        # 2) Andere Bibliotheken einbinden, die im Projekt - wie auch immer - referenziert werden
        sClasspathFileDirectory = os.path.join(sProjectPath, "target", "classpathZZZ")
        
        # 2a) ZKernelFileCollection Bibliotheksabhängigkeiten des Projekts einbinden.
        # Diese sind relativ zum Eclipse Workspace angegeben. Dieser Pfad wird über meine Batch beim Eclipsestart gesetzt.
        # Mehrere Pfade werden mit Semikolon getrennt.
        # Z.B.: \ZKernelFileCollection\commons-lang-2.1.jar
        #
        # Wichtig: zusätzliche Argument sWorkspace am Ende
        # Beispiel: r"..\..\Projekt_Kernel02_JAZKernelEngine\JAZKernelEngine\target\classpathZZZ\classpathOfLibrariesWorkspaceZZZ.txt", sWorkspace
        sWorkspaceFile = os.path.join(sClasspathFileDirectory, "classpathOfLibrariesWorkspaceZZZ.txt")
        
        # 2b) Maven-Abhängigkeiten des Projekts einbinden.
        # Diese sind als absoluter Pfad angegeben, mehrere Pfade mit Semikolon getrennt.
        # Beispiel: r"..\..\Projekt_Kernel02_JAZKernelEngine\JAZKernelEngine\target\classpathZZZ\classpathOfLibrariesByMavenZZZ.txt"       
        sMavenFile = os.path.join(sClasspathFileDirectory, "classpathOfLibrariesByMavenZZZ.txt")
        
        # 2c) 
        sExternalFile = os.path.join(sClasspathFileDirectory, "classpathOfLibrariesExternalZZZ.txt")

        # 3) Lade die Libraries, die in den oben definierten Dateien erfasst sind. Entweder als absoluten Pfad, oder als Pfad relativ zum Workspace 
        iAdded = 0
        iAdded += self.oLoader.addClasspathFile(sWorkspaceFile, self.sWorkspace)
        iAdded += self.oLoader.addClasspathFile(sMavenFile)
        iAdded += self.oLoader.addClasspathFile(sExternalFile)
        return iAdded > 0

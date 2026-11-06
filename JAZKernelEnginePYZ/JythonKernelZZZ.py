# -*- coding: utf-8 -*-
"""Initializes Jython's Java classpath for one or more Eclipse projects."""

import os


class JythonKernelZZZ(object):

    def __init__(self, sWorkspace=None, oLoader=None):
        # MY_DATA is the Eclipse workspace root used by the generated
        # workspace-relative classpath files.
        self.sWorkspace = sWorkspace or os.environ.get("MY_DATA")
        if not self.sWorkspace:
            raise Exception("Umgebungsvariable MY_DATA nicht gesetzt!")
        self.sWorkspace = os.path.abspath(self.sWorkspace)

        from JavaClasspathLoaderZZZ import JavaClasspathLoaderZZZ
        self.oLoader = oLoader or JavaClasspathLoaderZZZ()
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
            # Erst aus dem Projekt zurück zum Root (Das ist der Root des Repositories)
            sProjectPath = os.path.join("..","..", sProjectPath) 
        return os.path.abspath(sProjectPath)

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

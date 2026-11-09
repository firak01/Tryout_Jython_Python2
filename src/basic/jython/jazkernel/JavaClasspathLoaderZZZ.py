# -*- coding: utf-8 -*-

'''
JavaClasspathLoader.py

Zentrale Verwaltung des Java-Classpaths für Jython 2.7.
Relative Pfade beziehen sich auf das Verzeichnis
dieser Python-Datei.

Created on 05.11.2026

@author: Fritz Lindhauer
'''

import os
import sys


class JavaClasspathLoaderZZZ(object):

    def __init__(self, sBasePath=None):

        if sBasePath is None:
            sBasePath = os.path.dirname(
                os.path.abspath(__file__)
            )

        self._sBasePath = os.path.abspath(sBasePath)
        self._loaded = []

    
    def resolvePath(self, sPath, sBasePath=None):
        """
        Löst einen relativen Pfad auf.
    
        Ohne sBasePath wird das Repository-Basisverzeichnis verwendet.
        Mit sBasePath wird das übergebene Basisverzeichnis verwendet.
        """
    
        if sBasePath is None:
            sBasePath = self._sBasePath
            
        sBasePathOffsetString = self.getBasePathOffsetString()
    
        if not os.path.isabs(sPath):
            sPath = os.path.join(sBasePath, sBasePathOffsetString, sPath)
            
        
        # NEIN: os.path.abspath: Sie bereinigt dabei auch redundante Elemente wie . (aktuelles Verzeichnis) oder .. 
        # return os.path.abspath(sPath)
        return sPath
    
    
    def resolveWorkspacePath(self, sPath, sWorkspacePath):
        """
        Löst einen Pfad relativ zum Eclipse Workspace auf.
    
        Unterstützt auch Einträge wie:
            \\ZKernelFileCollection\\commons-lang-2.1.jar
    
        Ein einzelner führender Backslash wird dabei als
        Workspace-relativer Pfad interpretiert.
        """
    
        if not sWorkspacePath:
            raise ValueError("Eclipse Workspace Pfad fehlt!")
    
        # Absolute Pfade mit Laufwerksbuchstaben oder UNC bleiben erhalten.
        sDrive, sTail = os.path.splitdrive(sPath)
    
        if sDrive:
            return os.path.abspath(sPath)
    
        # Ein einzelner führender Backslash bedeutet hier:
        # relativ zum Workspace, nicht zum Laufwerksstamm.        
        sPath = sPath.rstrip("\\/")
        sPath = sPath.lstrip("\\/") #falls man doppelt hinzugefügt hätte
            
       
        
        # NEIN: os.path.abspath: Sie bereinigt dabei auch redundante Elemente wie . (aktuelles Verzeichnis) oder .. 
        #sPathFinalTotal =  os.path.abspath(
        #    os.path.join(sWorkspacePath, sPath)
        #)
        sPathFinalTotal = os.path.join(sWorkspacePath, sPath)
        return sPathFinalTotal


    def addPath(self, sPath):
        """
        Fügt ein Verzeichnis oder eine JAR-Datei
        zum Jython-Suchpfad hinzu.
        """

        if sPath is None:
            return False

        sPath = self.resolvePath(sPath)

        if not os.path.exists(sPath):
            print("Classpath-Eintrag nicht gefunden: " + sPath)
            return False

        sPathNormalized = os.path.normcase(sPath)

        for sExisting in sys.path:
            if os.path.normcase(os.path.abspath(sExisting)) == sPathNormalized:
                return True

        sys.path.append(sPath)
        self._loaded.append(sPath)

        print("Classpath hinzugefügt: " + sPath)
        return True

    def addPaths(self, aPaths):

        iCount = 0

        for sPath in aPaths:
            if self.addPath(sPath):
                iCount += 1

        return iCount

    
    def addClasspathFile(self, sFilename, sWorkspacePath=None):
        """
        Liest eine Classpath-Datei ein.
    
        sFilename:
            Pfad zur Classpath-Datei.
            Relativ zum Repository-Basisverzeichnis.
    
        sWorkspacePath:
            Optionaler Eclipse Workspace Pfad.
            Wenn angegeben, werden die Einträge der
            Classpath-Datei relativ zum Workspace aufgelöst.
        """
    
        sFilename = self.resolvePath(sFilename)
    
        if not os.path.isfile(sFilename):
            print("Classpath-Datei nicht gefunden: " + sFilename)
            return 0
    
        f = open(sFilename, 'r')
    
        try:
            sClasspath = f.read().strip()
        finally:
            f.close()
    
        if not sClasspath:
            return 0
    
        # Windows: Semikolon als Trennzeichen
        aPaths = sClasspath.split(';')
    
        iCount = 0
    
        for sPath in aPaths:
    
            sPath = sPath.strip()
    
            if not sPath:
                continue
    
            
    
            # Workspace-relative Pfade           
            if sWorkspacePath is not None:               
                sPath = self.resolveWorkspacePath(
                    sPath,                    
                    sWorkspacePath
                )
    
            # Maven-Pfade bzw. bereits aufgelöste Pfade
            if self.addPath(sPath):
                iCount += 1
    
        return iCount


    def getLoadedPaths(self):
        return list(self._loaded)

    def getBasePath(self):
        return self._sBasePath
    
    def getBasePathOffset(self):
        # TODOGOON20261109 depth ausrechnen
        depth=5
        return depth
        
    def getBasePathOffsetString(self):
        depth = self.getBasePathOffset()
        sDepth='..\\' * depth
        return sDepth
    
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

    def resolvePath(self, sPath):
        """
        Löst einen relativen Pfad relativ zum Basisverzeichnis auf.
        """

        if not os.path.isabs(sPath):
            sPath = os.path.join(self._sBasePath, sPath)

        return os.path.abspath(sPath)

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

    def addClasspathFile(self, sFilename):
        """
        Liest eine Maven-Classpath-Datei ein.
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

        aPaths = sClasspath.split(os.pathsep)

        # Maven-Pfade sind normalerweise absolut.
        # Falls relative Pfade enthalten sind,
        # werden sie ebenfalls relativ zum Basisverzeichnis aufgelöst.

        return self.addPaths(aPaths)

    def getLoadedPaths(self):
        return list(self._loaded)

    def getBasePath(self):
        return self._sBasePath
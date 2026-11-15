# -*- coding: utf-8 -*-

'''
Created on 15.11.2026

@author: Fritz Lindhauer
'''

import os


# Hier käme die vor der Klasse definerte Methode hin, die dann zur staticMethod wird, bei der Methodic mit staticmethod(computePackageDepth)
# def computePackageDepth(sFilePath, sProjectPath):
def test4staticMethod():
    print("Static Method")  
    
# Die eigentliche Klasse
class ReflectCodeJYZ(object):
    
    def __init__(self):
            pass
               
    # Methodik wenn die Methode vorher, oben schon definert ist
    # computePackageDepth = staticmethod(computePackageDepth) 
    test4staticMethod = staticmethod (test4staticMethod())
    
    # Hier aber besser (auch weil Java ähnlicher) mit dem Decorator zu arbeiten
    @staticmethod    
    def computePackageDepth(sFilePathTotal, sProjectPath):
        """
        Berechnet die Verzeichnistiefe einer Python-Datei
        relativ zum Projektverzeichnis.
    
        Die Verzeichnisse werden gezählt, nicht die Datei selbst.
        """
        
        sRelativePath = os.path.relpath(sFilePathTotal, sProjectPath)
    
        sDirectory = os.path.dirname(sRelativePath)
    
        if not sDirectory:
            return 0
    
        return len(sDirectory.split(os.sep))
    
    @staticmethod
    def computWorkspaceDepth(sFilePathTotal, sProjectPath):
        iPackageDepth = ReflectCodeJYZ.computePackageDepth(sFilePathTotal, sProjectPath)
        iPackageDepth += 1
        return iPackageDepth
    
    
        
        
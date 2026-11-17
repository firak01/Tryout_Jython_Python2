# -*- coding: utf-8 -*-

'''
Created on 17.11.2026

@author: Fritz Lindhauer
'''

# Hier käme die vor der Klasse definerte Methode hin, die dann zur staticMethod wird, bei der Methodic mit staticmethod(computePackageDepth)
# def computePackageDepth(sFilePath, sProjectPath):
def test4staticMethod():
    print("Static Method")  
    
# Die eigentliche Klasse
class FileEasyJYZ(object):
    
    def __init__(self):
            pass
               
    # Methodik wenn die Methode vorher, oben schon definert ist
    # computePackageDepth = staticmethod(computePackageDepth) 
    test4staticMethod = staticmethod (test4staticMethod())
    
    # Hier aber besser (auch weil Java ähnlicher) mit dem Decorator zu arbeiten
    @staticmethod    
    def extract_directory_first(sFilePathTotal, sFilePathPrefix):
        """
        Hole das erste Verzeichnis nach dem angegebenen Pfad.
        """
        # Gemeinsamen Anfang entfernen
        sRemaining = sFilePathTotal[len(sFilePathPrefix):]

        # Am Trennzeichen aufteilen
        sDelimiter="\\"
        aParts = sRemaining.split(sDelimiter)

        # Das zweite Element zurückgeben
        if len(aParts) >= 2:
            return aParts[1]

        return None
       
    
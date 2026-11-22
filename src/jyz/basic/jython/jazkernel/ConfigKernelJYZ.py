# -*- coding: utf-8 -*-

'''
Created on 22.11.2026

@author: Fritz Lindhauer
'''

import os

# Hier käme die vor der Klasse definerte Methode hin, die dann zur staticMethod wird, bei der Methodic mit staticmethod(computePackageDepth)
# def computePackageDepth(sFilePath, sProjectPath):
def test4staticMethod():
    print("import gemacht: " + os.path.abspath(__file__)) 
    
# Die eigentliche Klasse
class ConfigKernelJYZ(object):
    
    def __init__(self):
            pass
               
    # Methodik wenn die Methode vorher, oben schon definert ist
    # computePackageDepth = staticmethod(computePackageDepth) 
    test4staticMethod = staticmethod (test4staticMethod())
    
    # Hier aber besser (auch weil Java ähnlicher) mit dem Decorator zu arbeiten
    @staticmethod    
    def getPathRepositoryLocal():
        """
        Hole den beim Eclipse Start als Umgebungsvariable erzeugten Wert.
        """
        repositoryLocal = os.environ.get("sRLZZZ")
        return repositoryLocal
       
    
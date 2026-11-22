# -*- coding: utf-8 -*-

'''
Created on 15.11.2026

@author: Fritz Lindhauer
'''

import os

# Hier käme die vor der Klasse definerte Methode hin, die dann zur staticMethod wird, bei der Methodic mit staticmethod(computePackageDepth)
# def computePackageDepth(sFilePath, sProjectPath):
def test4staticMethod():
    print("import gemacht: " + os.path.abspath(__file__)) 
    
# Die eigentliche Klasse
class ArrayUtilJYZ(object):
    
    def __init__(self):
            pass
               
    # Methodik wenn die Methode vorher, oben schon definert ist
    # computePackageDepth = staticmethod(computePackageDepth) 
    test4staticMethod = staticmethod (test4staticMethod())
    
    # Hier aber besser (auch weil Java ähnlicher) mit dem Decorator zu arbeiten
    @staticmethod    
    def createArray(element, iTimes):
        """
        Erstelle ein Array mit iTimes mal das Element
        """
        aReturn = []
        
        for i in range(iTimes):
            aReturn.append(element)
       
        return aReturn
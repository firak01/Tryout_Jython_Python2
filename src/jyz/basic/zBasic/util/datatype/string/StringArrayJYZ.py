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
class StringArrayJYZ(object):
    
    def __init__(self):
            pass
               
    # Methodik wenn die Methode vorher, oben schon definert ist
    # computePackageDepth = staticmethod(computePackageDepth) 
    test4staticMethod = staticmethod (test4staticMethod())
    
    # Hier aber besser (auch weil Java ähnlicher) mit dem Decorator zu arbeiten
    @staticmethod    
    def implode(elementArray, sSeperator):
        """
        Das Array wird zu einem String zusammengefasst.
        Die Elemente des Arrays sind mit dem Separator - String voneinander getrennt        
        """
        sReturn = ""   
        i=0
        iTimes = len(elementArray)    
        for i in range(iTimes):
            if(i<iTimes):
                sReturn+=elementArray[i]+sSeperator
       
        return sReturn
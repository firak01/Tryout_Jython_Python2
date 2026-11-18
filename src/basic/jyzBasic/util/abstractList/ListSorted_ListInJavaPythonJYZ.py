# -*- coding: utf-8 -*-

'''
Created on 18.11.2026

Aus dem Buch "Python 3, das umfassende Handbuch", Kapitel 19, Code Beispiel 11

Hier als Jython Beispiel für Vererbung.

Hier für Jython2.7 laufähig gemacht:
- Python2 unterstützt den Parameterlosen Aufruf von super() nicht (erst Python3)

- In Python 2.7 ermittelt super() die Methoden anhand der Python-MRO (Method Resolution Order).

- Jython bildet zwar die Java-Vererbung in seine Klassenhierarchie ein, 
  aber die Java-Methoden werden nicht in jedem Fall über das von Python erwartete 
  super()-Verhalten aufgelöst.
  
  ALSO: 
  super(ListSorted_ListInJavaJYZ, self).add(value) #geht nicht
  self.add(value)                                  #verwende also den direkten Weg und gehe nicht über super...
  
   

@author: Fritz Lindhauer
'''

import os

# Classpath konfigurieren
# Das reicht, da in __init__.py der JythonKernelZZZ "nach aussen kommuniziert" wird.
from basic.jython.jazkernel import *
oJythonKernel = JythonKernelJYZ()
oJythonKernel.addProject('JAZKernelEngine', 'Projekt_Kernel02_JAZKernelEngine\JAZKernelEngine')
oJythonKernel.loadProjectPaths()

from basic.jyzBasic.util.abstractList import *
from basic.zBasic.util.abstractList import ArrayListZZZ

# Hier käme die vor der Klasse definerte Methode hin, die dann zur staticMethod wird, bei der Methodic mit staticmethod(computePackageDepth)
# def computePackageDepth(sFilePath, sProjectPath):
def test4staticMethod():
    print("import gemacht: " + os.path.abspath(__file__)) 
    
# Die Jython Klasse erbt von der Java Klasse
# Bei Mehrfachvererbung...
#        Hier ist es entscheidend welche Klasse oben zuerst genannt wird als Superklasse.
#        Durch das Vertauschen der Elternklassen oben tauchen im Debug String die 
#        im Java Test übergebenen Werte auf, bzw. umgekehrt. 
# In den Methoden wird die unsortierte Methode der Java - Klasse aufgerufen.
# Daher muss erneut sortiert werden.
#
# Nur bei der imul - Methode wird die sortierte Methode der Python Klasse verwendet.
class ListSorted_ListInJavaJYZ(ArrayListZZZ, ListSortedPYZ):
    def __init__(self, *args, **kwargs):
        #Merke Python2 unterstützt den Parameterlosen Aufruf von super() nicht (erst Python3) 
        #super().__init__(*args, **kwargs)
        super(ListSorted_ListInJavaJYZ, self).__init__(*args, **kwargs)
        #self.sort()
        
    def append(self, value):
        #Merke Python2 unterstützt den Parameterlosen Aufruf von super() nicht (erst Python3)
        #super().append(value)
        # Das ist eine ListSortedPYZ Methode
        # super(ListSorted_ListInJavaJYZ, self).append(value)
        
        # Das ist die Liste Java Methode, gehe den direkten Weg und nicht über super...
        # Geht nicht: super(ListSorted_ListInJavaJYZ, self).add(value)
        self.add(value)
        self.sort()

        
    def extend(self, sequence):
        #Merke Python2 unterstützt den Parameterlosen Aufruf von super() nicht (erst Python3)
        #super().extend(sequence)
        
        # Das ist eine ListSortedPYZ Methode
        #super(ListSorted_ListInJavaJYZ, self).extend(sequence)
        
        # Das ist die Liste Java Methode, gehe den direkten Weg und nicht über super...
        # Geht nicht: super(ListSorted_ListInJavaJYZ, self).addAll(sequence)
        self.addAll(sequence)
        self.sort()


    def insert(self, index, value):
        #Merke Python2 unterstützt den Parameterlosen Aufruf von super() nicht (erst Python3)
        #super().insert(index, value)
        
        # Das ist eine ListSortedPYZ Methode
        #super(ListSorted_ListInJavaJYZ, self).insert(index, value)
        
        # Das ist die Liste Java Methode, gehe den direkten Weg und nicht über super...
        # Geht nicht: super(ListSorted_ListInJavaJYZ, self).add(index, value)
        self.add(index, value)
        self.sort()


    def reverse(self):
        raise NotImplementedError(
            "ListSorted_ListInPythonJYZ cannot be reversed"
        )

    def __iadd__(self, s):
        #Merke Python2 unterstützt den Parameterlosen Aufruf von super() nicht (erst Python3)
        #erg = super().__iadd__(s)
        
        # Das ist eine ListSortedPYZ Methode
        #erg = super(ListSorted_ListInJavaJYZ, self).__iadd__(s)
       
        # Das ist die Liste Java Methode, gehe den direkten Weg und nicht über super... 
        # Geht nicht: super(ListSorted_ListInJavaJYZ, self).add(s)
        self.add(s)
        self.sort()
        return self
    
    def __imul__(self, n):
        # Merke: __imul__ steht für In-place Multiplication (Multiplikation an Ort und Stelle).
        # Das ist also z.B. a*3  was einem a=a*3 entspicht.
       
        '''
        wohl reine Python Funktionalität, hier wieder drin, implementiere mit Mehrfachvererbung Java,Python
        '''
        
        #Merke Python2 unterstützt den Parameterlosen Aufruf von super() nicht (erst Python3)
        #erg = super().__imul__(n)
        erg = super(ListSortedPYZ, self).__imul__(n)
        #self.sort()
        return erg

'''
# Code zum Test am Schluss, nur wenn diese Klasse direkt gestartet wird
if __name__ == "__main__":
    l = ListSorted_ListInJavaJYZ([6, 4, 3])
    
    # 1. Java-Methode direkt aufrufen
    l.add(6666)
    
    # 2. Java-Methode über die eigene Python-Methode aufrufen
    l.append(7777)
    
    # 3. Java-Methode als Methodenreferenz ausgeben
    print(l.add)
    
    print("Java Methoden Aufruf:")
    l.computeDebugString()  
'''



# Code zum Test am Schluss, nur wenn diese Klasse direkt gestartet wird
if __name__ == "__main__":
    l = ListSorted_ListInJavaJYZ([6, 4, 3])
    
    # Test nun eine Funktion der Java Klasse
    # Beachte diese Werte sind nicht einsortiert
    print("Java Test 01")
    l.add(6666)
    l.addUnique(7777)
    print(l)
    print(type(l))
    print(l.getClass().getName())
    print("Java Werte, debugString:    " ,l.computeDebugString)
    
    # Baechte diese Werte sind sortiert
    l.append(2)
    print(l)
    print(type(l))
    print(l.getClass().getName())
    
    l.extend([67, 0, -56])
    print(l)
    print(type(l))
    print(l.getClass().getName())
    
    l += [100, 5]
    print(l)   
    print(type(l))
    print(l.getClass().getName())
     
    #imu - inplace Multiplikator
    l *= 2
    print(l)   
    print(type(l))
    print(l.getClass().getName())
    
    #Fehler
    #print("Python Werte, debugString:    " ,l.computeDebugString)
    #AttributeError: 'instancemethod' object has no attribute 'computeDebugString'
    print("Python Werte, debugString:    " ,l.computeDebugString)

    # Test nun eine Funktion der Java Klasse
    # Beachte, diese Werte sind nicht einsortiert
    print("Java Test 02")
    l.add(6666)
    l.addUnique(7777) #da vorher schon mal 7777 eingegeben wurde darf das nicht aufgenommen werden.
    print(type(l))
    print(l)
    print("Java Werte, debugString:    " ,l.computeDebugString)

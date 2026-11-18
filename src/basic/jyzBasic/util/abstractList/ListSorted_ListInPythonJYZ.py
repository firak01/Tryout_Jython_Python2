# -*- coding: utf-8 -*-

'''
Created on 18.11.2026

Aus dem Buch "Python 3, das umfassende Handbuch", Kapitel 19, Code Beispiel 11

Hier als Jython Beispiel für Vererbung.

Hier für Jython2.7 laufähig gemacht:
- Python2 unterstützt den Parameterlosen Aufruf von super() nicht (erst Python3)

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
    
# Die Jython Klasse erbt von der Python Klasse
# UND Jython Klasse erbt von der Java Klasse
class ListSorted_ListInPythonJYZ(ListSortedPYZ, ArrayListZZZ):
    def __init__(self, *args, **kwargs):
        #Merke Python2 unterstützt den Parameterlosen Aufruf von super() nicht (erst Python3) 
        #super().__init__(*args, **kwargs)
        super(ListSorted_ListInPythonJYZ, self).__init__(*args, **kwargs)
        #self.sort()

    def __setitem__(self, key, value):
        #Merke Python2 unterstützt den Parameterlosen Aufruf von super() nicht (erst Python3)
        #super().__setitem__(key, value)        
        super(ListSorted_ListInPythonJYZ, self).__setitem__(key, value)
        #self.sort()

    def append(self, value):
        #Merke Python2 unterstützt den Parameterlosen Aufruf von super() nicht (erst Python3)
        #super().append(value)
        super(ListSorted_ListInPythonJYZ, self).append(value)
        #self.sort()

    def extend(self, sequence):
        #Merke Python2 unterstützt den Parameterlosen Aufruf von super() nicht (erst Python3)
        #super().extend(sequence)
        super(ListSorted_ListInPythonJYZ, self).extend(sequence)
        #self.sort()

    def insert(self, index, value):
        #Merke Python2 unterstützt den Parameterlosen Aufruf von super() nicht (erst Python3)
        #super().insert(index, value)
        super(ListSorted_ListInPythonJYZ, self).insert(index, value)
        #self.sort()

    def reverse(self):
        raise NotImplementedError(
            "ListSorted_ListInPythonJYZ cannot be reversed"
        )

    def __iadd__(self, s):
        #Merke Python2 unterstützt den Parameterlosen Aufruf von super() nicht (erst Python3)
        #erg = super().__iadd__(s)
        erg = super(ListSorted_ListInPythonJYZ, self).__iadd__(s)
        #self.sort()
        return erg

    def __imul__(self, n):
        # Merke: __imul__ steht für In-place Multiplication (Multiplikation an Ort und Stelle).
        # Das ist also z.B. a*3  was einem a=a*3 entspicht.
       
        #Merke Python2 unterstützt den Parameterlosen Aufruf von super() nicht (erst Python3)
        #erg = super().__imul__(n)
        erg = super(ListSorted_ListInPythonJYZ, self).__imul__(n)
        #self.sort()
        return erg

# Code zum Test am Schluss, nur wenn diese Klasse direkt gestartet wird
if __name__ == "__main__":
    l = ListSorted_ListInPythonJYZ([6, 4, 3])
    print(l)
    l.append(2)
    print(l)
    l.extend([67, 0, -56])
    print(l)
    l += [100, 5]
    print(l)
    l *= 2
    print(l)
    
    # Test nun eine Funktion der Java Klasse
    print("Java Test")
    l.add(6666)
    l.addUnique(7777)
    print(l)
    print("Java Werte, debugString:    " ,l.computeDebugString)
    # FAZIT: Die Methoden der Java-Klasse stehen zur Verfügung
    # ABER   Das Hinzufügen funktioniert nicht
    #        Die Werte werden wohl in der PYTHON Liste gehalten.
    

# -*- coding: utf-8 -*-

'''
Created on 04.11.2026

@author: Fritz Lindhauer
'''

'''
Created on 16.10.2026

@author: Fritz Lindhauer
'''
from java.lang import System

#Binde den Classpath ein
import sys
#sys.path.append(r"C:\MeinWorkspace\MeinJavaProjekt\bin")
sys.path.append(r"C:\1fgl\repo\EclipseOxygen_V02\Projekt_Kernel02_JAZKernelEngine\JAZKernelEngine\target\classes")

from basic.zBasic.util.datatype.string import StringZZZ

print("Java-Version:")
print(System.getProperty("java.version"))

print("Aktueller Zeitstempel:")
print(System.currentTimeMillis())



qString='das ist toll'
result = StringZZZ.capitalize(qString)
print(result)

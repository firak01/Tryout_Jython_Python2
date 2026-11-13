# -*- coding: utf-8 -*-

'''
Created on 04.11.2026

@author: Fritz Lindhauer
'''

#Binde den Classpath ein
import sys
#sys.path.append(r"C:\MeinWorkspace\MeinJavaProjekt\bin")
sys.path.append(r"C:\1fgl\repo\EclipseOxygen_V02\Projekt_Kernel02_JAZKernelEngine\JAZKernelEngine\target\classes")


from java.lang import System

print("Java-Version:")
print(System.getProperty("java.version"))

print("Classpath:")
print(System.getProperty("java.class.path"))


#Binde den Classpath ein
#import sys
#sys.path.append(r"C:\MeinWorkspace\MeinJavaProjekt\bin")
#sys.path.append(r"C:\1fgl\repo\EclipseOxygen_V02\Projekt_Kernel02_JAZKernelEngine\JAZKernelEngine\target\classes")

#print("new Classpath:")
#print(System.getProperty("java.class.path"))
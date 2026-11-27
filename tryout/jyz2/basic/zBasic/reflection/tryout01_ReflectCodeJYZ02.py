# -*- coding: utf-8 -*-

'''
Created on 15.11.2026

@author: Fritz Lindhauer
'''

from jyz.basic.zBasic.reflection import *


sProjectPath = r"C:\1fgl\repo\EclipseOxygen_V02\Tryout_Jython_Python2"
sFilePathTotal = r"C:\1fgl\repo\EclipseOxygen_V02\Tryout_Jython_Python2\tryout\PYZKernelEngineJAZ\tryout04_LogZZZ.py"

iPackageDepth = ReflectCodeJYZ.computePackageDepth(sFilePathTotal, sProjectPath)

# Kommt sauber beim python run als Ausdruck heraus 
# print("Pakettiefe: ", iDirectoryDepth)

# So kommt es sauber beim jython run als Ausdruck heraus
# Beim python run Fehlermeldung: SyntaxError: Missing parentheses in call to 'print'
print "Pakettiefe: %s" %iPackageDepth
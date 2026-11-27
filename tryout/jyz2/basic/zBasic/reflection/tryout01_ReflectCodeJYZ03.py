# -*- coding: utf-8 -*-

'''
Created on 15.11.2026

@author: Fritz Lindhauer
'''

import os
from jyz.basic.zBasic.reflection import *


print('File name :        ', os.path.basename(__file__))
print('Directory Name:    ', os.path.dirname(__file__))
print('absPath():         ', os.path.abspath(__file__))

#sFilePathTotal = r"C:\1fgl\repo\EclipseOxygen_V02\Tryout_Jython_Python2\tryout\PYZKernelEngineJAZ\tryout04_LogZZZ.py"
sFilePathTotal=os.path.abspath(__file__)
print('sFilePathTotal:      ', sFilePathTotal)

#sProjectPath = r"C:\1fgl\repo\EclipseOxygen_V02\Tryout_Jython_Python2"
sRepoPath = os.getenv("sRLZZZ")
print('sRepoPath (sRLZZZ): ', sRepoPath )

sProjectDirectory = "" #Hier keines, sonst fangen die Project Directories immer mit "Project_" an
print('sProjectDirectory:  ', sProjectDirectory )

sProjectName = "Tryout_Jython_Python2"
print('sProjectName:  ', sProjectName )



#sProjectPath = sRepoPath + "\\" + sProjectDirectory + "\\" + sProjectName
sProjectPath = sRepoPath + "\\" + sProjectName
print('sProjectPath:  ', sProjectPath )




iPackageDepth = ReflectCodeJYZ.computePackageDepth(sFilePathTotal, sProjectPath)

# Kommt sauber beim python run als Ausdruck heraus 
# print("Pakettiefe: ", iDirectoryDepth)

# So kommt es sauber beim jython run als Ausdruck heraus
# Beim python run Fehlermeldung: SyntaxError: Missing parentheses in call to 'print'
print "Pakettiefe: %s" %iPackageDepth
# -*- coding: utf-8 -*-

'''
Created on 15.11.2026

@author: Fritz Lindhauer
'''

from jyz.basic.zBasic.util.file import *


sRepoPath = r"C:\1fgl\repo\EclipseOxygen"
sFilePathTotal = r"C:\1fgl\repo\EclipseOxygen\Tryout_Jython_Python2\tryout\PYZKernelEngineJAZ\tryout04_LogZZZ.py"

sProjectName = FileEasyJYZ.extract_directory_first_byDirectoryPath(sFilePathTotal, sRepoPath)

# Kommt sauber beim python run als Ausdruck heraus 
# print("Pakettiefe: ", iDirectoryDepth)

# So kommt es sauber beim jython run als Ausdruck heraus
# Beim python run Fehlermeldung: SyntaxError: Missing parentheses in call to 'print'
print "Projektname: %s" %sProjectName
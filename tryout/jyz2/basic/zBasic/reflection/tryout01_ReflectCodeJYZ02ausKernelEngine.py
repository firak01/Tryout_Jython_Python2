# -*- coding: utf-8 -*-

'''
Created on 15.11.2026

@author: Fritz Lindhauer
'''

from jyz.basic.zBasic.reflection import *

sFilePathTotal = r"C:\1fgl\repo\EclipseOxygen\Project_JYZKernelEngine\JYZKernelEngine\tryout\jyz\basic\zBasic\reflection\tryout01_ReflectCodeJYZ02.py"
print('sFilePathTotal:      ', sFilePathTotal)

sProjectPath =   r"C:\1fgl\repo\EclipseOxygen\Project_JYZKernelEngine\JYZKernelEngine"
print('sProjectPath:  ', sProjectPath )

iPackageDepth = ReflectCodeJYZ.computePackageDepth(sFilePathTotal, sProjectPath)

# Kommt sauber beim python run als Ausdruck heraus 
# print("Pakettiefe: ", iDirectoryDepth)

# So kommt es sauber beim jython run als Ausdruck heraus
# Beim python run Fehlermeldung: SyntaxError: Missing parentheses in call to 'print'
print "Pakettiefe: %s" %iPackageDepth
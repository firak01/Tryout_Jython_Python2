# -*- coding: utf-8 -*-

'''
Created on 18.11.2026

@author: Fritz Lindhauer
'''


# Classpath konfigurieren
# Das reicht, da in __init__.py der JythonKernelZZZ "nach aussen kommuniziert" wird.
from jyz.basic.jython.jazkernel import *
oJythonKernel = JythonKernelJYZ()
oJythonKernel.addProject('JAZKernelEngine', 'Projekt_Kernel02_JAZKernelEngine\JAZKernelEngine')
oJythonKernel.loadProjectPaths()


from jyz.basic.zBasic.util.abstractList import *

if __name__ == "__main__":
    l = ListSortedPYZ([6, 4, 3])
    print(l)
    l.append(2)
    print(l)
    l.extend([67, 0, -56])
    print(l)
    l += [100, 5]
    print(l)
    l *= 2
    print(l)
# -*- coding: utf-8 -*-

'''
Created on 21.11.2026

@author: Fritz Lindhauer
'''

import sys

#Ausgabe der python-pfade
for sPath in sys.path:
    print(sPath)


# Importe aus PYZKernelEngine. 
# Es wird nur der im Projektpfad als erstes definierte Sourcefolder gezogen.
from pyz.basic.zBasic.util.math.PotenzPYZ import PotenzPYZ

#Instanziere die Klasse mit dem passenden Namen
hoch3 = PotenzPYZ(3)

#Wende das an, als "vom Namen her sprechende" Methode
erg01 = hoch3(2)    
print("2 hoch 3: ", erg01) 

erg02 = hoch3(5)    
print("5 hoch 3: ", erg02) 

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
''' Dieser Import schlägt immer fehl
    from pyz import HelloTryoutPYZ
    ImportError: cannot import name 'HelloTryoutPYZ'
    
from pyz import HelloTryoutPYZ
'''
from pyz import HelloSrcPYZ


objHalloSrc = HelloSrcPYZ()
erg00b = objHalloSrc.compute('Welt')
print("erg00b:", erg00b)

''' Dieser Code wird mangel funktionierenden Import nie ausführbar.
    ImportError: cannot import name 'HelloTryoutPYZ'

objHalloTryout = HelloTryoutPYZ()
erg00a = objHalloTryout.compute('Welt')
print("erg00a:", erg00a)
'''


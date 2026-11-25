#from __future__ statement required for example to work
from __future__ import nested_scopes

def outerFunc(x, y):
    def innerFunc(z):
        if z > 0:
            print z, y
            innerFunc(z - 1)
    innerFunc(x)
    
outerFunc(3, "fred")


class MyClass:
    
    def __init__(self):
        self._private = 1
        self.__reallyprivate = 2
        
    def printPrivateValues(self):
        print self._private, self.__reallyprivate
        
x = MyClass()
x.printPrivateValues()
print x._private
try:
    print x.__reallyprivate
except:
    print "No attribute named x.__reallyprivate"  
print x._MyClass__reallyprivate


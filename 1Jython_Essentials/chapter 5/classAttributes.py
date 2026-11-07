class MyClass:
    
    instancesCreated = 0
    
    def __init__(self, initialValue=0):
        MyClass.instancesCreated += 1
        self.value = initialValue
        
x = MyClass()
print x.instancesCreated
y = MyClass()
print x.instancesCreated
print MyClass.instancesCreated


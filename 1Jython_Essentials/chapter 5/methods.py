class MyClass:
    
    def __init__(self, initialValue=0):
        self.counter = initialValue
        
    def incrementCounter(self, amountToIncrement=1):
        self.counter += amountToIncrement
        
print MyClass.__dict__    

x = MyClass(3)
print x.counter

x.incrementCounter()
print x.counter
print x.__dict__



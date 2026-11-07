class AssociateFunction:
    
    def __init__(self):
        self._thing = 1
        
    def getThing(self):
        return float(self._thing)
    
    def __getattr__(self, attribute):
        if attribute == "thing":
            return self.getThing()
        else:
            raise AttributeError(attribute)           
x = AssociateFunction()
print x.thing
print x.nothing


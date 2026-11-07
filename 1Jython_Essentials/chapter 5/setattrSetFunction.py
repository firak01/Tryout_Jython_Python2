class SetFunction:
    
    def __init__(self):
        self.integerAttribute = 12
        self.otherAttribute = "herman"
        
    def setIntegerAttribute(self, value):
        value = int(value)
        if value < 0:
            value *= -1
        self.__dict__["integerAttribute"] = value
        
    def __setattr__(self, name, value):
        if name == "integerAttribute":
            self.setIntegerAttribute(value)
        else:
            self.__dict__[name] = value
            
x = SetFunction()
x.otherAttribute = -3
print x.otherAttribute
x.integerAttribute = -3
print x.integerAttribute


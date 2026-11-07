class Immutable:
    
    def __init__(self, **args):
        for key, value in args.items():
            self.__dict__[key] = value
            
    def __setattr__(self, name, value):
        raise TypeError, "Cannot change values: %s" % name
        
x = Immutable(one=1)
print x.one
x.one = 2


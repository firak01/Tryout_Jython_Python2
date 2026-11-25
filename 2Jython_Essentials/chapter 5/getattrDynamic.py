class DynamicAttributes:

    def __init__(self, **args):
        self.vals = args
        
    def __getattr__(self, attribute):
        return self.vals[attribute]
        
x = DynamicAttributes(fred="flintstone", barney="rubble")
print x.fred
print x.barney
x.vals["george"] = "jetson"
print x.george


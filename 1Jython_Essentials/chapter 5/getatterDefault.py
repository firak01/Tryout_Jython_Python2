class GetAttrExample:

    def __init__(self):
        self.attribute = 3
        
    def __getattr__(self, attribute):
        return 0
        
x = GetAttrExample()
print x.attribute
print x.fred


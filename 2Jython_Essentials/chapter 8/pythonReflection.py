class ParentClass:
    def __init__(self, parentValue):
        self.parentValue = parentValue
        
    def speak(self):
        print "I am a parent"
        
class ChildClass(ParentClass):
    def __init__(self, parentValue, childValue):
        ParentClass.__init__(self, parentValue)
        self.childValue = childValue
        
    def play(self):
        print "I can play"
        
childInstance = ChildClass(1, 2) 
       
print "__dict__:", childInstance.__dict__
print "dir:", dir(childInstance)
print "vars:", vars(childInstance)
print "__class__:", childInstance.__class__
print

print "__bases__:", ChildClass.__bases__
print "class __dict__:", ChildClass.__dict__
print "class dir:", dir(ChildClass)

def methodsOf(aClass):
    classMembers = vars(aClass).values()
    methods = [eachMember for eachMember in classMembers 
            if callable(eachMember)]
    for eachBase in aClass.__bases__:
        methods.extend(methodsOf(eachBase))
    return methods
    
print methodsOf(ChildClass)


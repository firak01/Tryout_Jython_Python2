class LivingThing:   
    def isAlive(self):
        print "Living Things are Alive"
                   
class Animal(LivingThing):   
    def canMove(self):
        print "Animals can move"
        
class ProgrammingLanguage:   
    def isAlive(self):
        print "Programming languages are not alive"
        
class Python(ProgrammingLanguage, Animal):   
    def isSlithery(self):
        print "Pythons slither"
        
x = Python()
x.isSlithery()
x.canMove()
x.isAlive()


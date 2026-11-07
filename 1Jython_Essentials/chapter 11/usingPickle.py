import pickle

class TestClass:
    
    def __init__(self, value=0):
        self.value = value
        self.message = "Serialized"
        
    def __str__(self):
        return "Message: %(message)s value: is %(value)s" % self.__dict__

instance = TestClass(3)
        
outFile = open("test.pickle", "w")
pickle.dump(instance, outFile)
outFile.close()

inFile = open("test.pickle")
readInstance = pickle.load(inFile)

print readInstance


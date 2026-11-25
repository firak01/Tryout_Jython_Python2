import java.io as io
import org.python.util as util

class TestClass(io.Serializable):
    
    def __init__(self, value=0):
        self.value = value
        self.message = "Serialized"
        
    def toString(self):
        return "Message: %(message)s value: is %(value)s" % self.__dict__
        
instance = TestClass(3)
        
outFile = io.FileOutputStream("test.ser")
outStream = io.ObjectOutputStream(outFile)
outStream.writeObject(instance)
outFile.close()

inFile = io.FileInputStream("test.ser")
inStream = util.PythonObjectInputStream(inFile)
readInstance = inStream.readObject()

print readInstance.toString()


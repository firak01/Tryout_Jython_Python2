import org.xml.sax as sax
parserClass = "org.apache.xerces.parsers.SAXParser"

def attrToDict(attrs):
    result = {}
    for i in range(attrs.length):
        result[attrs.getLocalName(i)] = attrs.getValue(i)
    return result

class RecipeHandler(sax.helpers.DefaultHandler):
    
    def __init__(self):
        self.ingredientCount = 0
        self.instructionCount = 0
    
    def startDocument(self):
        print "Printing A Recipe"
        
    def do_name(self, attrs):
        print "Recipe Name:",
    
    def do_ingredient(self, attrs):
        attrDict = attrToDict(attrs)
        if not self.ingredientCount:
            print "\nIngredients:" 
        self.ingredientCount += 1
        print attrDict["amount"], attrDict["unit"],
         
    def do_instruction(self, attrs):
        if not self.instructionCount:
            print "\nInstructions:"
        self.instructionCount += 1
        print "%s. " % (self.instructionCount), 
    
    def startElement(self, namespaceURI, localName, qName, attrs):
        method = getattr(self, "do_" + localName, lambda x: None)
        method(attrs)
            
    def characters(self, chars, start, length):
        print ''.join(chars[start:start+length]).strip(),
        
    def endElement(self, namespaceURI, localName, qName):
        print
        
    def endDocument(self):
        print "\n\nEnjoy!"

if __name__ == '__main__':
    reader = sax.helpers.XMLReaderFactory.createXMLReader(parserClass)
    inputSource = sax.InputSource("recipe.xml")
    reader.contentHandler = RecipeHandler()
    reader.parse(inputSource)


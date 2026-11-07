import org.w3c.dom as dom
import org.apache.xerces as xerces
import java.io as io

def printDocument(domDoc):
    print "Printing a Recipe"
    rootElement = domDoc.documentElement
    nameElement = rootElement.getElementsByTagName("name").item(0)
    print "Recipe Name: %s" % nameElement.firstChild.nodeValue.strip()
    
    print "\n\nIngredients:"
    ingredientNodes = rootElement.getElementsByTagName("ingredient")
    for i in range(ingredientNodes.length):
        node = ingredientNodes.item(i)
        print "%s %s %s" % (node.attributes.getNamedItem("amount").value,
                node.attributes.getNamedItem("unit").value,
                node.firstChild.nodeValue.strip())

    print "\n\nInstructions"
    instructionNodes = rootElement.getElementsByTagName("instruction")
    for i in range(instructionNodes.length):
        node = instructionNodes.item(i)
        print "%s. %s" % (i + 1, node.firstChild.nodeValue.strip())
    print "\n\nEnjoy!"
        

if __name__ == "__main__":
    parser = xerces.parsers.DOMParser()
    parser.parse("recipe.xml")
    printDocument(parser.document)


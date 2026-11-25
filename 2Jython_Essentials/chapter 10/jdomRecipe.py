import org.jdom as jdom
import java.io as io

def printDocument(jdomDoc):
    print "Printing a Recipe"
    rootElement = jdomDoc.rootElement
    nameElement = rootElement.getChild("name")
    print "Recipe Name: %s" % (nameElement.textTrim)
    
    print "\n\nIngredients:"
    for node in rootElement.getChildren("ingredient"):
        print "%s %s %s" % (node.getAttribute("amount").value,
                node.getAttribute("unit").value, node.textTrim)

    print "\n\nInstructions"
    counter = 1
    for node in rootElement.getChildren("instruction"):
        print "%s. %s" % (counter, node.textTrim)
        counter += 1
    print "\n\nEnjoy!"

if __name__ == "__main__":
    builder = jdom.input.SAXBuilder()
    doc = builder.build(io.FileInputStream("recipe.xml"))
    printDocument(doc)


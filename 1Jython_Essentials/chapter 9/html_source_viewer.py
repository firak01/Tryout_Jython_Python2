import htmllib
import formatter
from pawt import swing
import java
import urllib

class HtmlTreeParser(htmllib.HTMLParser):
    
    def __init__(self, initialText = ""):
        htmllib.HTMLParser.__init__(self, formatter.NullFormatter(), 0)
        self.model = HtmlTagTreeModel()
        self.tagStack = []
        self.feed(initialText)
     
    def currentTag(self):
        if self.tagStack:
            return self.tagStack[len(self.tagStack) - 1]
        
    def handle_starttag(self, tag, method, attrs):
        self.starttag(tag, attrs)
    
    def unknown_starttag(self, tag, attrs): 
        self.starttag(tag, attrs)
    
    def starttag(self, tag, attrs):
        tag = Tag(tag, attrs)
        if not self.model.rootTag:
            self.model.rootTag = tag
        if self.tagStack:
            self.currentTag().addChild(tag)
        self.tagStack.append(tag)

    def handle_endtag(self, tag, method):
        self.endtag(tag)
    
    def unknown_endtag(self, tag): 
        self.endtag(tag)
    
    def endtag(self, tag):
        poppedTags = []
        while 1:
            poppedTag = self.tagStack.pop()
            if poppedTag.tagString == tag:
                break
            else:
                poppedTag.myParent.addChildren(poppedTag.children)
                poppedTag.children = []
 
    def handle_data(self, data):
        data = data.strip()
        if data:
            self.currentTag().children.append(data)
            
class Tag(java.lang.Object):
    
    def __init__(self, tagString, attrs=[]):
        self.tagString = tagString
        self.children = []
        self.data = "" 
        self.arguments = attrs
        self.arguments.sort()
        self.myParent = None
        
    def addChild(self, newChild):
        self.children.append(newChild)
        if isinstance(newChild, Tag):
            newChild.myParent = self
        
    def addChildren(self, children):
        for each in children:
            self.addChild(each)
            
    def argumentString(self):
        stringList = ["%s = %s" % (key, value) 
                for key, value in self.arguments]
        return ', '.join(stringList)
    
    def toString(self):
        string = "<%s>" % self.tagString
        if self.arguments:
            string += self.argumentString()
        return string
    
    def __str__(self):
        return toString(self)

class HtmlTagTreeModel(swing.tree.TreeModel):
    
    def __init__(self):
        self.rootTag = None
    
    def addTreeModelListener(self, listener): pass
    def removeTreeModelListener(self, listener): pass
    def valueForPathChanged(path, newValue): pass
        
    def getChild(self, parent, index):
        return parent.children[index]
        
    def getChildCount(self, parent):
        return len(parent.children)
        
    def getIndexOfChild(self, parent, child):
        return parent.children.index(child)
        
    def getRoot(self):
        return self.rootTag
        
    def isLeaf(self, node):
        return (type(node) == type("")) or (len(node.children) == 0)

class HtmlTreeViewer(swing.JFrame):
    
    def __init__(self, htmlString="", url=""):
        swing.JFrame.__init__(self, title="HTML Source Browser", 
                size=(400, 600))
        if url:
            connection = urllib.urlopen(url)
            htmlString = connection.read()
        self.parser = HtmlTreeParser(htmlString)
        self.tree = swing.JTree(model=self.parser.model)
        scrollpane = swing.JScrollPane(self.tree)
        self.contentPane.add(scrollpane)
        
if __name__ == "__main__":\
    HtmlTreeViewer(url="http://www.jython.org").show()



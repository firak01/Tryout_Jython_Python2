import unittest
from html_source_viewer import *

class HtmlSourceViewerTest(unittest.TestCase):
    
    basicText = '''<html><head><title>Test Page</title></head>
            <body>
            <h2 align='center'>This is my test page</h2>
            <table border='1' align="left"><tr><td>0</td><td>1</td></tr></table>
            <ul><li>fred<li>barney<b>is</b>a friend</ul>
            <a href="www.jython.org">jython</a>
            </body>
            </html>''' 
            
    def setUp(self):
        "Create the HtmlParser and model"
        self.htmlParser = HtmlTreeParser(self.basicText)     
        self.model = self.htmlParser.model
            
    def testStackComplete(self):
        "Ensure that everything is off the stack after parsing"
        self.assertEqual(0, len(self.htmlParser.tagStack))
    
    def assertTag(self, tag, expectedName, expectedChildren, arguments=[]):
        "Assert that a tag has expected values"
        self.assertEqual(expectedName, tag.tagString)
        self.assertEqual(expectedChildren, self.model.getChildCount(tag))
        self.assertEqual(expectedChildren == 0, self.model.isLeaf(tag))
        self.assertEqual(arguments, tag.arguments)
        
    def assertLeaf(self, leaf, expectedString):
        "Assert that a leaf has expected values"
        self.assertEqual(expectedString, leaf)
        self.assert_(self.model.isLeaf(leaf))
    
    def testRoot(self):
        "Test that the root is set correctly"
        root = self.model.getRoot()
        self.assertEqual(2, len(root.children))
        self.assertTag(root, "html", 2)
        
    def testHead(self):
        "Test that the head tag is set correctly, first test of traversal"
        root = self.model.getRoot()
        headTag = self.model.getChild(root, 0)
        self.assertTag(headTag, "head", 1)     
        titleTag = self.model.getChild(headTag, 0)
        self.assertTag(titleTag, "title", 1)
        titleString = self.model.getChild(titleTag, 0)
        self.assertLeaf(titleString, "Test Page")
        
    def testBody(self):
        "Test the main body tag -- first test of attributes"
        root = self.model.getRoot()
        bodyTag = self.model.getChild(root, 1)
        self.assertTag(bodyTag, "body", 4)
        headerTag = self.model.getChild(bodyTag, 0)
        self.assertTag(headerTag, "h2", 1, [("align", "center")])
        
    def testTable(self):
        "Test the table tag -- multiple attributes, and traversal"
        root = self.model.getRoot()
        bodyTag = self.model.getChild(root, 1)
        tableTag = self.model.getChild(bodyTag, 1)
        self.assertTag(tableTag, "table", 1, 
                [("align", "left"), ("border", "1")])
        trTag = self.model.getChild(tableTag, 0)
        self.assertTag(trTag, "tr", 2)
        
    def testUl(self):
        "Test the ul tag -- single tags, and interspaced text and tags"
        root = self.model.getRoot()
        bodyTag = self.model.getChild(root, 1)
        ulTag = self.model.getChild(bodyTag, 2)
        self.assertTag(ulTag, "ul", 6)
        for i in [0, 2]:
            liTag = self.model.getChild(ulTag, i)
            self.assertTag(liTag, "li", 0)
        bTag = self.model.getChild(ulTag, 4)
        self.assertTag(bTag, "b", 1)
        self.assertEqual(["is"], bTag.children)
    
def suite():
    suite = unittest.makeSuite(HtmlSourceViewerTest)
    return suite        
    
if __name__ == '__main__':
    unittest.main()    


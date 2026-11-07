import javax.swing as swing
import java

ACTIVATED = swing.event.HyperlinkEvent.EventType.ACTIVATED
ENTERED = swing.event.HyperlinkEvent.EventType.ENTERED
EXITED = swing.event.HyperlinkEvent.EventType.EXITED

class HtmlBrowserWindow(swing.JFrame):
    
    def __init__(self, urlString="http://www.jython.org"):
        swing.JFrame.__init__(self, title="HTML Browser", size=(800, 600))
        self.contentPane.layout = java.awt.BorderLayout()
        self.contentPane.add(self.buildTopPane(urlString),
                java.awt.BorderLayout.NORTH)
        self.htmlPane = swing.JEditorPane(urlString, editable=0,
                hyperlinkUpdate=self.followHyperlink, size=(400,400))
        self.contentPane.add(swing.JScrollPane(self.htmlPane),
                java.awt.BorderLayout.CENTER)
        self.status = swing.JLabel(" ", preferredSize=(500,20))
        self.contentPane.add(self.status, java.awt.BorderLayout.SOUTH)

    def buildTopPane(self, startUrl):
        label = swing.JLabel("Go To:")
        self.field = swing.JTextField(preferredSize=(500,20),
                text=startUrl, actionPerformed=self.goToUrl)
        button = swing.JButton("Go", size=(100,100), 
                actionPerformed=self.goToUrl)
        topPane = swing.JPanel()
        topPane.add(label)
        topPane.add(self.field)
        topPane.add(button)
        return topPane
    
    def goToUrl(self, event):
        self.htmlPane.setPage(self.field.text)
        
    def followHyperlink(self, hlEvent):
        if hlEvent.eventType == ACTIVATED:
            self.htmlPane.setPage(hlEvent.URL)
            self.field.text = hlEvent.URL.toString()
        elif hlEvent.eventType == ENTERED:
            self.status.text = hlEvent.URL.toString()
        elif hlEvent.eventType == EXITED:
            self.status.text = " "
        
if __name__ == "__main__":
    HtmlBrowserWindow().show()


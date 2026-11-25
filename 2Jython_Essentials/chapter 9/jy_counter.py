import javax.swing as swing
import java

class Counter(swing.JFrame):

    def __init__(self):
        swing.JFrame.__init__(self, title="Counter", size=(200, 100))
        self.contentPane.layout = java.awt.FlowLayout()
        self.value = 0
        
        self.display = swing.JTextField(preferredSize=(200, 30), 
                horizontalAlignment=swing.SwingConstants.CENTER)
        self.setDisplay()
        self.contentPane.add(self.display)  
        
        increment = swing.JButton("Inc", size=(65, 70),
                actionPerformed=self.incrementDisplay)
        self.contentPane.add(increment)
        
        clear = swing.JButton("Clear", size=(65, 70),
                actionPerformed=self.clearDisplay)       
        self.contentPane.add(clear)
        
        decrement = swing.JButton("Dec", size=(65, 70),
                actionPerformed=self.decrementDisplay)       
        self.contentPane.add(decrement)

    def incrementDisplay(self, event):
        self.value += 1
        self.setDisplay()
        
    def decrementDisplay(self, event):
        self.value -= 1
        self.setDisplay()
        
    def clearDisplay(self, event):
        self.value = 0
        self.setDisplay()
    
    def setDisplay(self):
        self.display.text = str(self.value)

if __name__ == "__main__":
    Counter().show()



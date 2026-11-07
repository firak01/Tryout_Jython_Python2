import java.lang as lang
import javax.swing as swing
import java.awt as awt

names = ["Groucho", "Chico", "Harpo"]
quotes = {"Groucho": "Say the secret word", 
        "Chico": "Viaduct?", "Harpo": "HONK!"}

def buttonPressed(event):
     field.text = quotes[event.source.text]

def exit(event):
    lang.System.exit(0)
     
def createButton(name):
    return swing.JButton(name, preferredSize=(100,20), 
            actionPerformed=buttonPressed)
    
win = swing.JFrame("Welcome to Jython", size=(200, 200),windowClosing=exit)
win.contentPane.layout = awt.FlowLayout()

field = swing.JTextField(preferredSize=(200,20))
win.contentPane.add(field)
 
buttons = [createButton(each) for each in names]
for eachButton in buttons:
    win.contentPane.add(eachButton)
win.pack()
win.show()


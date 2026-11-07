import WelcomeFrame;
import javax.swing.JButton;

public class FrameUser {
    public static void main(String[] argv) {
        WelcomeFrame f = new WelcomeFrame("From Java");
        JButton newButton = f.createButton("Zeppo");
        f.addQuote("Zeppo", "Hello");
        f.getContentPane().add(newButton);
        f.pack();
        f.show();
    }
}


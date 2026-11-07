import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class Counter extends JFrame {

    private JTextField display;
    private int value;
    
    public Counter(){
        this.getContentPane().setLayout(new java.awt.FlowLayout());
        value = 0;
        this.setTitle("Counter");
        this.setSize(200, 100);
        
        this.display = new JTextField();
        this.display.setPreferredSize(new Dimension(200, 30));
        this.setDisplay();
        this.display.setHorizontalAlignment(SwingConstants.CENTER);
        this.getContentPane().add(display);   
        
        JButton increment = new JButton("Inc");
        increment.setSize(65, 70);
        increment.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent evt) {
                Counter.this.value++;
                Counter.this.setDisplay();
            }
        }
        );
        this.getContentPane().add(increment);
        
        JButton clear = new JButton("Clear");
        clear.setSize(65, 70);
        clear.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent evt) {
                Counter.this.value = 0;
                Counter.this.setDisplay();
            }
        });
        this.getContentPane().add(clear);
        
        JButton decrement = new JButton("Dec");
        decrement.setSize(65, 70);
        decrement.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent evt) {
                Counter.this.value--;
                Counter.this.setDisplay();
            }
        });
        this.getContentPane().add(decrement);
    }
    
    private void setDisplay() {
        this.display.setText(String.valueOf(value));
    }
    
    public static void main(String[] args) {
        Counter window = new Counter();
        window.show();
    }
}


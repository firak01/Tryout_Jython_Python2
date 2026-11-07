public class OverloadExample {
 
    public void method(long l) {
        System.out.print("long method: ");
        System.out.println(l);
    }
    
    public void method(int i) {
        System.out.print("int method: ");
        System.out.println(i);
    }
    
    public void method(String s) {
        System.out.print("string method: ");
        System.out.println(s);
    }
    public void method(Object o) {
        System.out.print("object method: ");
        System.out.println(o);
    }
    
    public void method(Object o1, Object o2) {
        System.out.print("two-argument method: ");
        System.out.println(o1.toString() + " " + o2.toString());
    }
     
}


public class JavaConstructorBase {

  protected JavaConstructorBase() {
    System.out.println("protected JavaBase()");
  }

  private String txt;

  public JavaConstructorBase(String txt) {
    System.out.println("public JavaBase(\""+txt+"\")"); 

    this.txt = txt;
  }

  public void setText(String txt) {
    this.txt = txt;
  }

  public String getText() { return txt; }

}



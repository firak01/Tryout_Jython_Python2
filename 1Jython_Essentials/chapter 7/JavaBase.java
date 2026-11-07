public class JavaBase {

  public String one() { return "Java-one"; };

  protected String two() { return "Java-two"; }


  public static String callOne(JavaBase jb) { return jb.one(); }
  public static String callTwo(JavaBase jb) { return jb.two(); }

}


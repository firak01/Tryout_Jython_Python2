public abstract class JavaAbstract {

  abstract public void behavior(int j);
  abstract public void behavior(String s);
  abstract protected void behavior(int j,String s);

  public static void testBehaviorInt(JavaAbstract jabs) {
    jabs.behavior(1);
  }

  public static void testBehaviorString(JavaAbstract jabs) {
    jabs.behavior("baz");
  }

  public static void testBehaviorIntString(JavaAbstract jabs) {
    jabs.behavior(1,"foo");
  }

}


/* 
Test with the following at the Jython prompt:

>>> import JavaAbstract
>>> class SnakeClass(JavaAbstract):
...   def behavior(self, *args):
...     print "got: %s" % (args,)
...
>>> snake=SnakeClass()
>>> JavaAbstract.testBehaviorInt(snake)
got: (1,)

>>> JavaAbstract.testBehaviorString(snake)
got: ('baz',)

>>> JavaAbstract.testBehaviorIntString(snake)
got: (1, 'foo')
*/

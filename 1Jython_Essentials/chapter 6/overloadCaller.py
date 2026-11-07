import OverloadExample
import java

x = OverloadExample()
x.method(3)
x.method(java.lang.Integer(3))
x.method("3")
x.method([1, 2])
x.method(1, 2)


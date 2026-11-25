import JavaBase

class SnakeClass(JavaBase):
  def __init__(self,opt):
    print "begin __init__"
    if opt == "default":
      pass
    elif opt == "explicit":
      JavaBase.__init__(self)
    elif opt == "force":
      self.setText("snake")
    elif opt == "error":
      self.setText("snake")
      JavaBase.__init__(self)
    else:
      JavaBase.__init__(self,opt)
    print "end __init__"

def try_snake(opt):
  print "*** SnakeClass(%r) ***" % opt
  snake = SnakeClass(opt)
  print snake.getText(), "\n"

try_snake("default")
try_snake("explicit")
try_snake("force")
try_snake("jython")
try_snake("error")


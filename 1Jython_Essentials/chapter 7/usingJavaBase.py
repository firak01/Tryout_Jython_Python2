import JavaBase

class SnakeClass(JavaBase):
  def one(self):
    return "snake-one(%s)" % self.super__two()

  def two(self):
    return "snake-two(%s)"  % JavaBase.one(self)


snake=SnakeClass()
print JavaBase.callOne(snake)
print JavaBase.callTwo(snake)


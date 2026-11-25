import SampleBean

sample = SampleBean()
print "dir:", dir(sample)
print "__class__:", sample.__class__

print "\n__bases__:", SampleBean.__bases__
print "class dir:", dir(SampleBean)
print "class vars:", vars(SampleBean)

print methodsOf(SampleBean)

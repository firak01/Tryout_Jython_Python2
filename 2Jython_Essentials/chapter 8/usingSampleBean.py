import SampleBean
beanInstance = SampleBean()

print beanInstance.stringProperty
print beanInstance.integerProperty

beanInstance.stringProperty += " and reset"
beanInstance.integerProperty += 1

print beanInstance.stringProperty
print beanInstance.integerProperty


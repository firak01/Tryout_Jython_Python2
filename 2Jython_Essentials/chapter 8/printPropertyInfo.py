import java.beans
import SampleBean

def printPropertyInfo(beanClass):
    info = java.beans.Introspector.getBeanInfo(beanClass)
    propertyArray = info.getPropertyDescriptors()
    for each in propertyArray:
        print each.name
        
printPropertyInfo(SampleBean)


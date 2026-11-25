import IndexBean
indexInstance = IndexBean()
print indexInstance.arrayProperty[1]
indexInstance.arrayProperty[2] = "fred"
print indexInstance.arrayProperty[2]

anotherInstance = IndexBean(arrayProperty=("a", "b", "c"))
print anotherInstance.arrayProperty[1]

#print indexInstance.arrayProperty[1]
#indexInstance.arrayProperty[2] = "fred"
#print indexInstance.arrayProperty[2]
# does not work! Instead use

print indexInstance.getArrayProperty(1)
indexInstance.setArrayProperty(2, "fred")
print indexInstance.getArrayProperty(2)


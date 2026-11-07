f = open("foo.txt",'w')
f.write("small\n")
f.writelines(["file\n","foo\n"])
f.close()
f = open("foo.txt",'r')
print f.readlines()
f.close()


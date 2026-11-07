import re
pattern = re.compile("ll")
target = "Hello, Allan"
lastLocation = 0
while 1:
    result = pattern.search(target, lastLocation)
    if not result: break
    print result.span()
    lastLocation = result.end()


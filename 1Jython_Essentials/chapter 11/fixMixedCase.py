import re
def fixMixedCase(thing):
    regex = re.compile("[a-z][A-Z]")
    pos = 0
    while 1:
        match = regex.search(thing, pos)
        if not match:
            break
        pos = match.start() + 1
        thing = thing[:pos] + ' ' + thing[pos:]    
    return thing   
    
print fixMixedCase("fixMixedCase")
print fixMixedCase("aVariableName")

def fixMixedCaseImproved(thing):
    return re.sub('([a-z])([A-Z])', r'\1 \2', thing)

print fixMixedCaseImproved("fixMixedCase")
print fixMixedCaseImproved("aVariableName")


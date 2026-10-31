'''
Created on 31.10.2026

@author: Fritz Lindhauer
'''

# The following function changes the text of a string by making a copy
# of the string and then altering it.  The original string is left
# untouched as it is immutable.
def changestr(mystr):
    mystr = mystr + '_changed'
    print 'The string inside the function: ', mystr
    
    # return the new String to use it outside
    return mystr
 
mystr = 'hello'
hello_changed=changestr(mystr)
print "The old string outside the function: %s ist wieder da" % mystr
print "The new string outside the function: %s ist wieder da" % hello_changed

from __future__ import nested_scopes

def tag_fun_maker(tag):
    open = "<%s" % tag
    close = "</%s>" % tag
    def tagfunc(*content, **attrs):
        attrs = ['%s="%s"' % (key, value) for key, value in attrs.items()]
        attrs = ' '.join(attrs)
        return "%s %s>%s%s" % (open,attrs,''.join(content),close)
    return tagfunc

html = tag_fun_maker("html")
body = tag_fun_maker("body")
strong = tag_fun_maker("strong")
anchor = tag_fun_maker("a")

print html(body(
    "\n", 
    anchor(strong("Hello World from Jython!"),
    href="http://www.jython.org"),
    "\n"))

#<html ><body >
#<a href="http://www.jython.org"><strong >Hello World from Jython!</strong></a>
#</body></html>


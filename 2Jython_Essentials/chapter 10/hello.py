import javax.servlet.http as http

class hello(http.HttpServlet):
     
     def doGet(self, request, response):
         response.contentType = "text/html"
         out = response.outputStream
         print >> out, "<h3>Hello World!</h3>"


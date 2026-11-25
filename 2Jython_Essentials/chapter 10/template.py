import javax.servlet.http as http
import time

class template(http.HttpServlet):
     
     def tempString(self, request):
         fileName = request.getParameter("file")
         try:
             template = open(self.servletContext.getRealPath("/%s.ptem" %           
                                                             fileName))
             return template.read()
         finally:
             template.close()
         
     def tempDict(self, request):
         timeTuple = time.localtime()
         result = {}
         result['date'] = time.strftime("%A, %B %d, %Y", timeTuple)
         result['time'] = time.strftime("%I:%M:%S %p", timeTuple)
         result['name'] = request.getParameter('name')
         return result
     
     def doGet(self, request, response):
         response.contentType = "text/html"
         out = response.outputStream
         print >> out, self.tempString(request) % self.tempDict(request)
         out.close()


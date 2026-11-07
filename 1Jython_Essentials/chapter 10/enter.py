import javax.servlet.http as http

class enter(http.HttpServlet):
     
     def doPost(self, request, response):
         session = request.getSession(1)
         counter = session.getAttribute("counter")
         try:
             counter = int(counter)
         except:  # counter is None
             counter = 0
         counter += 1
         session.setAttribute("counter", counter)
         out = response.outputStream
         print >> out, """The string you entered is: %s. <br> 
            You have played this game %s times.<hr>""" % (
            request.getParameter("thing"), counter)
         self.doGet(request, response)
     
     def doGet(self, request, response):
         response.contentType = "text/html"
         out = response.outputStream
         print >> out, """Enter a string: <form method="post">
             <input type="text" name="thing"><input  type="submit">   
             </form>"""
         


import javax.servlet.http as http

class reset(http.HttpServlet):
     def doGet(self, req, res):
         req.getAttribute("pyservlet").reset()
         req.getRequestDispatcher("/index.py").forward(req, res)


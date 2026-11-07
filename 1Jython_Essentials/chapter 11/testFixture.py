import unittest
import ftplib
class FtpTest(unittest.TestCase):
    
    def setUp(self):
        self.host = "ftp3.sourceforge.net"
        self.ftp = ftplib.FTP(self.host)
        self.ftp.login()
        
    def tearDown(self):
        self.ftp.close()
       
    def testPwd(self):
        self.assertEqual("/", self.ftp.pwd())
        
    def testWelcomeStatus(self):
        self.assertEqual("220", self.ftp.getwelcome()[:3])

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    stringSuite = unittest.makeSuite(FtpTest)
    runner.run(stringSuite)


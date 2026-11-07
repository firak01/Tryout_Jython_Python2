import unittest
class StringTest(unittest.TestCase):
    def runTest(self):
        self.assertEqual(4, len("hello"))
            
if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(StringTest())


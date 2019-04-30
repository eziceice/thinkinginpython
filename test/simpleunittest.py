import unittest, Test.Simple_doctest

def product(x, y):
    return x*y

class ProducTestCase(unittest.TestCase):

    def testIntegers(self):
        for x in range(-10,10):
            for y in range(-10,10):
                p = Test.Simple_doctest.square(x, y)
                self.failUnless(p == x*y, 'Integer multiplication failed')

    def testFloats(self):
        for x in range(-10,10):
            for y in range(-10,10):
                x = x/10.0
                y = y/10.0
                p = Test.Simple_doctest.square(x, y)
                self.failUnless(p == x*y, 'Float multiplication failed')

if __name__ == '__main__':
    unittest.main()
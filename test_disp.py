#!/usr/bin/python3 

class I:
    'imported objects'
    import unittest
    import disp
    import obj

disp = I.disp.default()

class Test(I.unittest.TestCase):    
    def test(self):  
        obj = I.obj.Param('parameter', 'TYPE', repr('abc'), 'My parameter for test')
        print(disp(obj))

if __name__ == '__main__':
    ttr = I.unittest.TextTestRunner(tb_locals=True)
    I.unittest.main(testRunner=ttr, verbosity=2)

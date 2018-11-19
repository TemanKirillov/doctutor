#!/usr/bin/python3 

class I:
    'imported objects'
    import unittest
    import obj
    import make
    import disp
    from repr import Repr

r = I.Repr()
m = I.make.Make()
def func(a, b = 1, c: 'param C' = 10) -> 'str':
    pass

class Test_Param(I.unittest.TestCase):    
    def test(self):  
        obj = m.Params(func)
        res = r.Param(obj[0])
        print(res)

class Test_Params(I.unittest.TestCase):    
    def test(self):  
        obj = m.Params(func)
        res = I.disp.recursive(obj)
        print(res)

if __name__ == '__main__':
    ttr = I.unittest.TextTestRunner(tb_locals=True)
    I.unittest.main(testRunner=ttr, verbosity=2)

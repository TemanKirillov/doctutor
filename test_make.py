#!/usr/bin/python3 

class I:
    'imported objects'
    import unittest
    import obj
    import make
    import collections.abc as abc

m = I.make.Make()
def func(a, b = 1, c: 'param C' = 10) -> 'str':
    pass
def func2(a, b = 1, c: 'param C' = 10):
    pass

class Test_Param(I.unittest.TestCase):    
    def test(self):  
        obj = m.Params(func)
        self.assertEqual(obj.a.name, 'a')
        self.assertEqual(obj.a.kind, 'POSITIONAL_OR_KEYWORD')
        self.assertEqual(obj.a.default, '')
        self.assertEqual(obj.a.desc, '')


class Test_Params(I.unittest.TestCase):    
    def test(self):  
        obj = m.Params(func)
        self.assertEqual(obj.b.name, 'b')
        self.assertEqual(obj.c.default, '10')
        self.assertEqual(obj.c.desc, 'param C')
        #test builtin function
        obj = m.Params(hex)
        self.assertEqual(obj.number.name, 'number')
        self.assertEqual(obj.number.kind, 'POSITIONAL_ONLY')
        self.assertEqual(obj.number.default, '')
        self.assertEqual(obj.number.desc, '')


class Test_Return(I.unittest.TestCase):    
    def test(self):  
        obj = m.Return(func)
        self.assertEqual(obj.desc, "'str'")
        #test without return annotation
        obj = m.Return(func2)
        self.assertEqual(obj.desc, '')
        #test builtin function
        obj = m.Return(hex)
        self.assertEqual(obj.desc, '')

if __name__ == '__main__':
    ttr = I.unittest.TextTestRunner(tb_locals=True)
    I.unittest.main(testRunner=ttr, verbosity=2)

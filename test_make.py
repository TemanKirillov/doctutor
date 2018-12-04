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
func.attr = 'attribute'
def func2(a, b = 1, c: 'param C' = 10):
    pass

class Test_Param(I.unittest.TestCase):    
    def test(self):  
        obj = m.Params(func)
        self.assertEqual(obj._.a._.name, 'a')
        self.assertEqual(obj._.a._.kind, 'POSITIONAL_OR_KEYWORD')
        self.assertEqual(obj._.a._.default, '')
        self.assertEqual(obj._.a._.desc, '')


class Test_Params(I.unittest.TestCase):    
    def test(self):  
        obj = m.Params(func)
        self.assertEqual(obj._.b._.name, 'b')
        self.assertEqual(obj._.c._.default, '10')
        self.assertEqual(obj._.c._.desc, 'param C')
        #test builtin function
        obj = m.Params(hex)
        self.assertEqual(obj._.number._.name, 'number')
        self.assertEqual(obj._.number._.kind, 'POSITIONAL_ONLY')
        self.assertEqual(obj._.number._.default, '')
        self.assertEqual(obj._.number._.desc, '')


class Test_Return(I.unittest.TestCase):    
    def test(self):  
        obj = m.Return(func)
        self.assertEqual(obj._.desc, "'str'")
        #test without return annotation
        obj = m.Return(func2)
        self.assertEqual(obj._.desc, '')
        #test builtin function
        obj = m.Return(hex)
        self.assertEqual(obj._.desc, '')

class Test_Attrs(I.unittest.TestCase):    
    def test(self):  
        obj = m.Attrs(func)
        self.assertEqual(obj._.attr, 'attribute')
        self.assertIs(obj._.__class__, func.__class__)


if __name__ == '__main__':
    ttr = I.unittest.TextTestRunner(tb_locals=True)
    I.unittest.main(testRunner=ttr, verbosity=2)

#!/usr/bin/python3 

class I:
    'imported objects'
    import unittest
    import obj
    import make
    import collections.abc as abc
    import string

m = I.make.Make()
def func(a, b = 1, c: 'param C' = 10) -> 'str':
    pass
func.attr = 'attribute'
def func2(a, b = 1, c: 'param C' = 10):
    pass

class Test_Attrs(I.unittest.TestCase):    
    def test(self):  
        obj = m.Attrs(func)
        self.assertEqual(obj._.attr, 'attribute')
        self.assertIs(obj._.__class__, func.__class__)

class Test_AttrsAll(I.unittest.TestCase):    
    def test(self):  
        obj = m.AttrsAll(func)
        [print(key, ':', value) for key, value in obj.items()]

class Test_ImportedAttrs(I.unittest.TestCase):    
    def test(self):  
        class T:
            import string

        obj = m.ImportedAttrs(I.string)
        self.assertEqual(list(obj.keys()), ['_type', '_ChainMap', '_re', '_string'])
        self.assertEqual(obj._._re, I.string._re)
        self.assertEqual(obj._._ChainMap, I.string._ChainMap)
        obj = m.ImportedAttrs(T)
        self.assertEqual(list(obj.keys()), ['_type', 'string'])
        self.assertEqual(obj._.string, I.string)


if __name__ == '__main__':
    ttr = I.unittest.TextTestRunner(tb_locals=True)
    I.unittest.main(testRunner=ttr, verbosity=2)

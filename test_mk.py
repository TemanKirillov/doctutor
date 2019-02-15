#!/usr/bin/python3 

class I:
    'imported objects'
    import unittest
    import obj
    import mk as make
    import collections.abc as abc
    import string

m = I.make.Make()
def func(a, b = 1, c: 'param C' = 10) -> 'str':
    pass
func.attr = 'attribute'
def func2(a, b = 1, c: 'param C' = 10):
    pass

class Test_Param(I.unittest.TestCase):    
    def test(self):  
        params = m.Params(func)
        obj = params['content']['a']
        oc = obj['content']
        self.assertEqual(obj['type'], 'Param')
        self.assertEqual(oc['name'], 'a')
        self.assertEqual(oc['kind'], 'POSITIONAL_OR_KEYWORD')
        self.assertEqual(oc['default'], '')
        self.assertEqual(oc['desc'], '')

class Test_Params(I.unittest.TestCase):    
    def test(self):  
        obj = m.Params(func)
        oc = obj['content']
        self.assertEqual(oc['b']['content']['name'], 'b')
        self.assertEqual(oc['c']['content']['default'], '10')
        self.assertEqual(oc['c']['content']['desc'], 'param C')
        #test builtin function
        obj = m.Params(hex)
        oc = obj['content']
        self.assertEqual(oc['number']['content']['name'], 'number')
        self.assertEqual(oc['number']['content']['kind'], 'POSITIONAL_ONLY')
        self.assertEqual(oc['number']['content']['default'], '')
        self.assertEqual(oc['number']['content']['desc'], '')

class Test_Return(I.unittest.TestCase):    
    def test(self):  
        obj = m.Return(func)
        self.assertEqual(obj['content'], "'str'")
        #test without return annotation
        obj = m.Return(func2)
        self.assertEqual(obj['content'], '')
        #test builtin function
        obj = m.Return(hex)
        self.assertEqual(obj['content'], '')

if __name__ == '__main__':
    ttr = I.unittest.TextTestRunner(tb_locals=True)
    I.unittest.main(testRunner=ttr, verbosity=2)

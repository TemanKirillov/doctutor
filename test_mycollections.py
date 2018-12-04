#!/usr/bin/python3 

class I:
    import unittest
    from mycollections import DictAttr
    from mycollections import GetAttrDict
    from collections import OrderedDict

class Test_GetAttrDict(I.unittest.TestCase):
    def test(self):
        dct = {'a': '1', 'b': '2'}
        gad = I.GetAttrDict(dct)
        self.assertEqual(gad.a, '1')
        self.assertEqual(gad.b, '2')
        with self.assertRaises(KeyError):
            gad.c

        class T(I.OrderedDict):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self._ = I.GetAttrDict(self)

        t = T(dct)
        self.assertEqual(t._.a, '1')
        self.assertEqual(t._.b, '2')
        t['c'] = '3'
        self.assertEqual(t._.c, '3')

        #__setattr__
        t._.c = '33'
        self.assertEqual(t._.c, '33')
        self.assertEqual(t['c'], '33')

        #__delattr__
        del t._.c
        with self.assertRaises(KeyError):
            t['c']
        with self.assertRaises(KeyError):
            t._.c

        #special attribute
        t['__class__'] = 'Test class'
        t._.__dict__ = 'Test dict'
        self.assertEqual(t._.__class__, 'Test class')
        self.assertEqual(t._.__dict__, 'Test dict')
        self.assertEqual(t['__class__'], 'Test class')
        self.assertEqual(t['__dict__'], 'Test dict')



class Test_DictAttr(I.unittest.TestCase):
    def test(self):
        t = I.DictAttr([('a', 'A')])
        self.assertEqual(t['a'], 'A')
        self.assertEqual(t.a, 'A')
        t.b = 'B'
        self.assertEqual(t['b'], 'B')
        self.assertEqual(t.b, 'B')
        t['c'] = 'C'
        self.assertEqual(t['c'], 'C')
        self.assertEqual(t.c, 'C')
        del t.c
        with self.assertRaises(AttributeError):
            t.c
        with self.assertRaises(KeyError):
            t['c']
        del t['b']
        with self.assertRaises(AttributeError):
            t.b
        with self.assertRaises(KeyError):
            t['b']

    def est_blacklist(self):
        t = I.DictAttr([('a', 'A')])
        self.assertEqual(str(t.__class__), "<class 'mycollections.DictAttr'>")
        t.__class__ = 'string.Template'
        self.assertEqual(t.__class__, 'string.Template')

if __name__ == '__main__':
    ttr = I.unittest.TextTestRunner(tb_locals=True)
    I.unittest.main(testRunner=ttr, verbosity=2)

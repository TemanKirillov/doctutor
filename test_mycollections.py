#!/usr/bin/python3 

class I:
    import unittest
    import inspect
    from mycollections import DictAttr
    import copy

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

    def test_blacklist(self):
        t = I.DictAttr([('a', 'A')])
        self.assertEqual(str(t.__class__), "<class 'mycollections.DictAttr'>")
        t.__class__ = 'string.Template'
        self.assertEqual(t.__class__, 'string.Template')
        t.__call__ = 'Call description'
        self.assertEqual(t.__call__, 'Call description')
        t.__dict__ = 'dict description'
        self.assertEqual(t.__dict__, 'dict description')
        for name, attr in I.inspect.getmembers(hex):
            t[name] = attr

    def test_deepcopy(self):
        t = I.DictAttr([('a', 'A')])
        t.b = 'B'
        t2 = I.copy.deepcopy(t)
        self.assertEqual(t2.b, 'B')
        self.assertEqual(t2['b'], 'B')
        t.b = 'C'
        self.assertEqual(t.b, 'C')
        self.assertEqual(t2.b, 'B')

if __name__ == '__main__':
    ttr = I.unittest.TextTestRunner(tb_locals=True)
    I.unittest.main(testRunner=ttr, verbosity=2)

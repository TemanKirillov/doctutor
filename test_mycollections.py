#!/usr/bin/python3 

class I:
    import unittest
    from mycollections import DictAttr

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

if __name__ == '__main__':
    ttr = I.unittest.TextTestRunner(tb_locals=True)
    I.unittest.main(testRunner=ttr, verbosity=2)

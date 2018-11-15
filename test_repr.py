#!/usr/bin/python3 

class I:
    'imported objects'
    import unittest
    from repr import Repr
    from repr import add_tab

class Test_add_tab(I.unittest.TestCase):

    def test(self):
        t = ' abc'
        self.assertEqual(I.add_tab(t), '\t abc')
        self.assertEqual(I.add_tab(t, 2), '\t\t abc')
        self.assertEqual(I.add_tab(t, 2, 2), '     abc')

class Test_Repr(I.unittest.TestCase):

    def test_Default(self):
        r = I.Repr()
        default = ('name', 'val', 'name for test')
        res = r.Default(default)
        print(res)

if __name__ == '__main__':
    ttr = I.unittest.TextTestRunner(tb_locals=True)
    I.unittest.main(testRunner=ttr, verbosity=2)


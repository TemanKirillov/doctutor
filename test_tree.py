#!/usr/bin/python3 

class I:
    'imported objects'
    import unittest
    from tree import ownattr
    from tree import any_fullmatch
    from tree import getmembers
    from tree import isimp
    from tree import isinparent

class Test_ownattr(I.unittest.TestCase):

    def test_builtin_func(self):
        gen = I.ownattr(hex)
        lst = list(gen)
        self.assertEqual(len(lst), 4)
        print('Вывод данных по встроенной функции:')
        [print(i) for i in lst]

    def test_user_func(self):

        def test(a,b):
            ''' test function'''
        test.attr = 8
        lst = list(I.ownattr(test))
        self.assertEqual(len(lst), 6)

    def test_class(self):

        class Test:
            ''' test class'''
            a = 8
            def __init__(self):
                self.b = 22
            def method(self):
                pass

        lst = list(I.ownattr(Test))
        self.assertEqual(len(lst), 9)

        inst = Test()
        inst.attr = 'test attr'
        lst = list(I.ownattr(inst))
        self.assertEqual(len(lst), 4)

    def test_module(self):
        import string as inst
        lst = list(I.ownattr(inst))
        self.assertEqual(len(lst), 22)
        print('Вывод данных по модулю:')
        [print(i[0]) for i in lst]

class Test_any_fullmatch(I.unittest.TestCase):
    
    def test_all(self):
        patterns = ['a', '\d\d', '.+__']
        self.assertTrue(I.any_fullmatch('a', *patterns))
        self.assertTrue(I.any_fullmatch('23', *patterns))
        self.assertFalse(I.any_fullmatch('b', *patterns))
        self.assertFalse(I.any_fullmatch('235', *patterns))

class Test_getmembers(I.unittest.TestCase):
    
    def test_isimp(self):
        import string
        print('Вывод импортированных объектов')
        gen = I.getmembers(string, I.isimp) 
        [print(i) for i in list(gen)]

if __name__ == '__main__':
    ttr = I.unittest.TextTestRunner(tb_locals=True)
    I.unittest.main(testRunner=ttr, verbosity=2)

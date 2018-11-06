#!/usr/bin/python3 

class I:
    'imported objects'
    import unittest
    from tree import ownattr

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
        self.assertEqual(len(lst), 7)

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
        self.assertEqual(len(lst), 25)
        print('Вывод данных по модулю:')
        [print(i[0]) for i in lst]

if __name__ == '__main__':
    ttr = I.unittest.TextTestRunner(tb_locals=True)
    I.unittest.main(testRunner=ttr, verbosity=2)

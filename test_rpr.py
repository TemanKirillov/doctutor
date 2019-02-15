#!/usr/bin/python3 

class I:
    'imported objects'
    import unittest
    from collections import OrderedDict
    import objs
    from rpr import Repr
    from rpr import add_tab
    from rpr import to_columns


class Test_add_tab(I.unittest.TestCase):
    TEST1 = 'test\n\tstring\n'
    TEST2 = '\ttest\n\tstring'

    def test_1(self):
        t = ' abc'
        self.assertEqual(I.add_tab(t), '\t abc')
        self.assertEqual(I.add_tab(t, 2), '\t\t abc')
        self.assertEqual(I.add_tab(t, 2, 2), '     abc')
    
    def test_2(self):    
        self.assertEqual(I.add_tab(self.TEST1), '\ttest\n\t\tstring\n')
        self.assertEqual(I.add_tab(self.TEST2), '\t\ttest\n\t\tstring')
        self.assertEqual(I.add_tab(self.TEST1, 2), '\t\ttest\n\t\t\tstring\n')

class Test_to_columns(I.unittest.TestCase):    
    def test(self):  
    
        print('='*50)
        print('Test to_columns:')
        text = I.to_columns(range(100), 4)
        print(text)
        
        print('='*50)
        print('Test to_columns with empty arg:')
        text = I.to_columns([], 4)
        print(text)

r = I.Repr()

class Test_Repr(I.unittest.TestCase):
    def test_Param(self):
        res = r.repr_by_obj(I.objs.Param1)
        print(res)
        #без значения по умолчанию и описания
        res = r.repr_by_obj(I.objs.Param2)
        print(res)

    def test_Params(self):
        res = r.repr_by_obj(I.objs.Params1)
        print(res)
        #пустой список
        res = r.repr_by_obj(I.objs.Params2)
        print(res)

    def test_Return(self):
        res = r.repr_by_obj(I.objs.Return1)
        print(res)

if __name__ == '__main__':
    ttr = I.unittest.TextTestRunner(tb_locals=True)
    I.unittest.main(testRunner=ttr, verbosity=2)


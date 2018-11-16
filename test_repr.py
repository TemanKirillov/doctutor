#!/usr/bin/python3 

class I:
    'imported objects'
    import unittest
    from repr import Repr
    from repr import add_tab
    from repr import to_columns

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

class Test_Repr(I.unittest.TestCase):
    def test_Default(self):
        r = I.Repr()
        default = ('name', 'val', 'name for test')
        res = r.Default(default)
        print(res)
        default = ('name', 'val', '')
        res = r.Default(default)
        print(res)

    def test_Param(self):
        r = I.Repr()
        obj = ('parameter', 'TYPE', repr('abc'), 'My parameter for test')
        res = r.Param(obj)
        print(res)
        #без значения по умолчанию и описания
        obj = ('parameter', 'TYPE', '', '')
        res = r.Param(obj)
        print(res)

    def test_Params(self):
        r = I.Repr()
        obj = ('Описание параметра 1', 'Описание параметра 2')
        res = r.Params(obj)
        print(res)
        #пустой список
        obj = []
        res = r.Params(obj)
        print(res)

    def test_Return(self):
        r = I.Repr()
        obj = ('None',)
        res = r.Return(obj)
        print(res)

    def test_Example(self):
        r = I.Repr()
        obj = ('<Example>',)
        res = r.Example(obj)
        print(res)

    def test_Except(self):
        r = I.Repr()
        obj = ('RuntimeError', 'Попытка операции на закрытом соединении.', '<Code>')
        res = r.Except(obj)
        print(res)

    def test_Exceptions(self):
        r = I.Repr()
        obj = ('Описание исключения 1', 'Описание исключения 2')
        res = r.Exceptions(obj)
        print(res)
        #пустой список
        obj = []
        res = r.Exceptions(obj)
        print(res)

    def test_Func(self):
        r = I.Repr()
        obj = ('hex', '(number)', 'Hexadecimal repr', 
               'number', 'string instance', '<Пример>', '<Исключения>')
        res = r.Func(obj)
        print(res)

    def test_Parents(self):
        r = I.Repr()
        obj = ('Описание родителя 1', 'Описание родителя 2')
        res = r.Parents(obj)
        print(res)
        #пустой список
        obj = []
        res = r.Parents(obj)
        print(res)

    def test_BlockOperators(self):
        r = I.Repr()
        obj = ('obj + other', '__dunder__', 'abc')
        res = r.BlockOperators(obj)
        print(res)
        #длинный список
        obj = range(0, 100)
        res = r.BlockOperators(obj)
        print(res)

    def test_GroupOperators(self):
        r = I.Repr()
        obj = ('string.Template', '__dunder__\nabc')
        res = r.GroupOperators(obj)
        print(res)
        #пустой список
        obj = ['string.Template', '']
        res = r.GroupOperators(obj)
        print(res)

    def test_Operators(self):
        r = I.Repr()
        obj = ( '__dunder__\nabc', '<Операторы родителя 1>', '<Операторы родителя 2>')
        res = r.Operators(obj)
        print(res)
        #пустой список собственных операторов
        obj = ['', '<Операторы родителя 1>' ]
        res = r.Operators(obj)
        print(res)
        #нет операторов
        obj = ['']
        res = r.Operators(obj)
        print(res)

if __name__ == '__main__':
    ttr = I.unittest.TextTestRunner(tb_locals=True)
    I.unittest.main(testRunner=ttr, verbosity=2)


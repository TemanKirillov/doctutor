#!/usr/bin/python3 

class I:
    'imported objects'
    import unittest
    from repr import Repr
    from repr import add_tab
    from repr import to_columns

class Test_Repr(I.unittest.TestCase):
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

    def test_GroupAttrs(self):
        r = I.Repr()
        obj = ('IMPORTED', '<Атрибут 1>')
        res = r.GroupAttrs(obj)
        print(res)
        #пустой список
        obj = ('IMPORTED', '')
        res = r.GroupAttrs(obj)
        print(res)

    def test_Class(self):
        r = I.Repr()
        obj = ('string.Template', 'A string class', 
               '<Parents>', '<init block>', '<Operators>', '<Attributes>')
        res = r.Class(obj)
        print(res)

    def test_Module(self):
        r = I.Repr()
        obj = ('string', 'A collection of string...', 
               '<Attributes>')
        res = r.Module(obj)
        print(res)

if __name__ == '__main__':
    ttr = I.unittest.TextTestRunner(tb_locals=True)
    I.unittest.main(testRunner=ttr, verbosity=2)


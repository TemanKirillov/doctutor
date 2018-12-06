#!/usr/bin/python3 

class I:
    'imported objects'
    import unittest
    from collections import OrderedDict
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

r = I.Repr()

class Test_Repr(I.unittest.TestCase):
    class Param1:
        class _:
            name = 'parameter' 
            kind = 'TYPE'
            default = repr('abc')
            desc = 'My parameter for test'

    class Param2:
        class _:
            name = 'parameter' 
            kind = 'TYPE'
            default = ''
            desc = ''

    Params1 = ['Описание параметра 1', 'Описание параметра 2']

    Params2 = []

    class Return1:
        class _:
            desc = 'None'

    class Func1:
        class _:
            name = 'hex'
            sign = '(number)'
            doc = 'Hexadecimal repr' 
            params = 'number'
            return_ = 'string instance'
            example = '<Пример>'
            exceptions = '<Исключения>'

    class Named1:
        class _:
            name = 'IMPORTED(Named1)'
            content = 'Атрибуты...'

    class Named2:
        class _:
            name = 'EMPTY(Named2)'
            content = ''

    class Block1:
        class _:
            name = 'IMPORTED(Block1)'
            desc = 'Импортированный инстументарий'
            content = 'Атрибуты...'

    class Block2:
        class _:
            name = 'EMPTY(Block2)'
            desc = ''
            content = ''


    def test_Default(self):
        default = ('name', 'val', 'name for test')
        res = r.Default(default)
        print(res)
        default = 5
        res = r.Default(default)
        print(res)

    def test_Param(self):
        res = r.Param(self.Param1)
        print(res)
        #без значения по умолчанию и описания
        res = r.Param(self.Param2)
        print(res)

    def test_Params(self):
        res = r.Params(self.Params1)
        print(res)
        #пустой список
        res = r.Params(self.Params2)
        print(res)

    def test_Return(self):
        res = r.Return(self.Return1)
        print(res)

    def test_Func(self):
        res = r.Func(self.Func1)
        print(res)

    def testAttrs(self):
        obj = ('<Атрибут 1>', '<Атрибут 2>')
        res = r.Attrs(obj)
        print(res)
        #пустой список
        obj = []
        res = r.Attrs(obj)
        print(res)

    def testImportedAttrs(self):
        obj = ('<Атрибут 1>', '<Атрибут 2>')
        res = r.ImportedAttrs(obj)
        print(res)
        #пустой список
        obj = []
        res = r.ImportedAttrs(obj)
        print(res)

    def testInternalAttrs(self):
        obj = ('<Атрибут 1>', '<Атрибут 2>')
        res = r.InternalAttrs(obj)
        print(res)
        #пустой список
        obj = []
        res = r.InternalAttrs(obj)
        print(res)

    def testOwnAttrs(self):
        obj = ('<Атрибут 1>', '<Атрибут 2>')
        res = r.OwnAttrs(obj)
        print(res)
        #пустой список
        obj = []
        res = r.OwnAttrs(obj)
        print(res)

    def testAttrsAll(self):
        obj = ('<Группа Атрибутов 1>', '<Группа Атрибутов 2>')
        res = r.AttrsAll(obj)
        print(res)
        #пустой список
        obj = []
        res = r.AttrsAll(obj)
        print(res)

    def test_Named(self):
        res = r.Named(self.Named1)
        print(res)
        #пустой 
        res = r.Named(self.Named2)
        print(res)

    def test_GroupAttrs(self):
        obj = ('IMPORTED', '<Атрибут 1>')
        res = r.GroupAttrs(obj)
        print(res)
        #пустой список
        obj = ('IMPORTED', '')
        res = r.GroupAttrs(obj)
        print(res)

    def test_Block(self):
        res = r.Block(self.Block1)
        print(res)
        #пустой блок
        res = r.Block(self.Block2)
        print(res)


if __name__ == '__main__':
    ttr = I.unittest.TextTestRunner(tb_locals=True)
    I.unittest.main(testRunner=ttr, verbosity=2)


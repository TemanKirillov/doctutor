#!/usr/bin/python3 

class I:
    'imported objects'
    import unittest
    import obj
    from repr import Repr

r = I.Repr()

class Test_Obj(I.unittest.TestCase):    
    def test(self):  
        o = I.obj.Obj()
        self.assertEqual(o._type, 'Obj')
        o.attr = 'test'
        self.assertEqual(o['attr'], 'test')
        o2 = I.obj.Obj([('a', '1'), ('b', '2')])
        self.assertEqual(o2.a, '1')
        self.assertEqual(o2._type, 'Obj')


class Test_Param(I.unittest.TestCase):    
    def test(self):  
        obj = I.obj.Param.from_iterable(('parameter', 'TYPE', repr('abc'), 'My parameter for test'))
        res = r.Param(obj)
        print(res)
        
class Test_Params(I.unittest.TestCase):    
    def test(self):  
        obj = I.obj.Params([('a', 'Описание параметра a'), ('b', 'Описание параметра b')])
        res = r.Params(obj)
        print(res)

class Test_Return(I.unittest.TestCase):    
    def test(self):  
        obj = I.obj.Return('None',)
        res = r.Return(obj)
        print(res)

class Test_Example(I.unittest.TestCase):    
    def test(self):  
        obj = I.obj.Example('<Example>',)
        res = r.Example(obj)
        print(res)

class Test_Except(I.unittest.TestCase):    
    def test(self):  
        obj = I.obj.Except('RuntimeError', 'Попытка операции на закрытом соединении.', '<Code>')
        res = r.Except(obj)
        print(res)

class Test_Exceptions(I.unittest.TestCase):    
    def test(self):  
        obj = I.obj.Exceptions(('Описание исключения 1', 'Описание исключения 2'))
        res = r.Exceptions(obj)
        print(res)

class Test_Func(I.unittest.TestCase):    
    def test(self):  
        obj = I.obj.Func('hex', '(number)', 'Hexadecimal repr', 'number', 'string instance', '<Пример>', '<Исключения>')
        res = r.Func(obj)
        print(res)

class Test_Parents(I.unittest.TestCase):    
    def test(self):  
        obj = I.obj.Parents(('Описание родителя 1', 'Описание родителя 2'))
        res = r.Parents(obj)
        print(res)

class Test_BlockOperators(I.unittest.TestCase):    
    def test(self):  
        obj = I.obj.BlockOperators(('obj + other', '__dunder__', 'abc'))
        res = r.BlockOperators(obj)
        print(res)

class Test_GroupOperators(I.unittest.TestCase):    
    def test(self):  
        obj = I.obj.GroupOperators('string.Template', '__dunder__\nabc')
        res = r.GroupOperators(obj)
        print(res)

class Test_Operators(I.unittest.TestCase):    
    def test(self):  
        obj = I.obj.Operators(( '__dunder__\nabc', '<Операторы родителя 1>', '<Операторы родителя 2>'))
        res = r.Operators(obj)
        print(res)

class Test_Attrs(I.unittest.TestCase):    
    def test(self):  
        obj = I.obj.Attrs(('<Атрибут 1>', '<Атрибут 2>'))
        res = r.Attrs(obj)
        print(res)

class Test_GroupAttrs(I.unittest.TestCase):    
    def test(self):  
        obj = I.obj.GroupAttrs('IMPORTED', '<Атрибут 1>')
        res = r.GroupAttrs(obj)
        print(res)

class Test_Class(I.unittest.TestCase):    
    def test(self):  
        obj = I.obj.Class('string.Template', 'A string class', '<Parents>', '<init block>', '<Operators>', '<Attributes>')
        res = r.Class(obj)
        print(res)

class Test_Module(I.unittest.TestCase):    
    def test(self):  
        obj = I.obj.Module('string', 'A collection of string...', '<Attributes>')
        res = r.Module(obj)
        print(res)

if __name__ == '__main__':
    ttr = I.unittest.TextTestRunner(tb_locals=True)
    I.unittest.main(testRunner=ttr, verbosity=2)

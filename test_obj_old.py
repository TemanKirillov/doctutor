#!/usr/bin/python3 

class I:
    'imported objects'
    import unittest
    import obj
    from repr import Repr

r = I.Repr()

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


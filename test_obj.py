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
        self.assertEqual(o._._type, 'Obj')
        o._.attr = 'test'
        self.assertEqual(o['attr'], 'test')
        o2 = I.obj.Obj([('a', '1'), ('b', '2')])
        self.assertEqual(o2._.a, '1')
        self.assertEqual(o2._._type, 'Obj')

class Test_Param(I.unittest.TestCase):    
    def test(self):  
        obj = I.obj.Param.from_iterable(('parameter', 'TYPE', repr('abc'), 'My parameter for test'))
        self.assertEqual(obj['name'], 'parameter')
        self.assertEqual(obj._.name, 'parameter')
        self.assertEqual(obj._.kind, 'TYPE')
        self.assertEqual(obj._.default, "'abc'")
        self.assertEqual(obj._.desc, "My parameter for test")
        
class Test_Params(I.unittest.TestCase):    
    def test(self):  
        obj = I.obj.Params([('a', 'Описание параметра a'), ('b', 'Описание параметра b')])
        self.assertEqual(obj._.a,  'Описание параметра a')
        self.assertEqual(obj._.b,  'Описание параметра b')

class Test_Return(I.unittest.TestCase):    
    def test(self):
        obj = I.obj.Return([('desc', 'None',)])
        self.assertEqual(obj._.desc,  'None')

class Test_Func(I.unittest.TestCase):    
    def test(self):  
        obj = I.obj.Func.from_iterable(['hex', '(number)', 'Hexadecimal repr', 'number', 'string instance', '<Пример>', '<Исключения>'])

class Test_Attrs(I.unittest.TestCase):    
    def test(self):  
        obj = I.obj.Attrs([('a','<Атрибут 1>'), ('b', '<Атрибут 2>')])
        self.assertEqual(obj._.a, '<Атрибут 1>')
        self.assertEqual(obj._.b, '<Атрибут 2>')

class Test_Named(I.unittest.TestCase):    
    def test(self):  
        obj = I.obj.Named([('name','Столица'), ('content', 'Москва')])
        self.assertEqual(obj._.name, 'Столица')
        self.assertEqual(obj._.content, 'Москва')

class Test_Block(I.unittest.TestCase):    
    def test(self):  
        obj = I.obj.Named([('name','IMPORTED'), ('desc', 'Импортированный инстументарий'), ('content', 'Атрибуты...')])
        self.assertEqual(obj._.name, 'IMPORTED')
        self.assertEqual(obj._.desc,  'Импортированный инстументарий')
        self.assertEqual(obj._.content, 'Атрибуты...')

class Test_GroupAttrs(I.unittest.TestCase):    
    def test(self):  
        obj = I.obj.GroupAttrs.from_iterable(('IMPORTED', '<Атрибут 1>'))
        self.assertEqual(obj._.name, 'IMPORTED')
        self.assertEqual(obj._.content,  '<Атрибут 1>')


if __name__ == '__main__':
    ttr = I.unittest.TextTestRunner(tb_locals=True)
    I.unittest.main(testRunner=ttr, verbosity=2)

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
        obj = I.obj.Return([('desc', 'None',)])
        res = r.Return(obj)
        print(res)

class Test_Func(I.unittest.TestCase):    
    def test(self):  
        obj = I.obj.Func.from_iterable(['hex', '(number)', 'Hexadecimal repr', 'number', 'string instance', '<Пример>', '<Исключения>'])
        res = r.Func(obj)
        print(res)

if __name__ == '__main__':
    ttr = I.unittest.TextTestRunner(tb_locals=True)
    I.unittest.main(testRunner=ttr, verbosity=2)

#!/usr/bin/python3 

class I:
    'imported objects'
    import unittest
    import disp
    import obj
    import make
    import string

disp = I.disp.default()

class Test(I.unittest.TestCase):    
    def test(self):  
        obj = I.obj.Param.from_iterable(('parameter1', 'TYPE', repr('abc'), 'My parameter for test'))
        print(disp(obj))

    def test_recurs(self):  
        obj1 = I.obj.Param.from_iterable(('parameter1', 'TYPE', repr('abc'), 'My parameter for test'))
        obj2 = I.obj.Param.from_iterable(('parameter2', 'TYPE', repr('abc'), 'My parameter for test'))
        obj3 = I.obj.Params({'p1':obj1, 'p2':obj2})
        print(I.disp.recursive(obj3))

        obj4 = I.obj.Params({'a': obj1, 'b':'<param2>'})
        print(I.disp.recursive(obj4))
        obj5 = I.obj.Params([('a', '<param1>'), ('b','<param2>')])
        print(I.disp.recursive(obj5))

    def test_Attrs(self):
        obj = I.make.Make().Attrs(I.string.Template)
        for key, value in obj.items():
            obj[key] = I.obj.GroupAttrs.from_iterable([str(key), repr(value)])
        print(I.disp.recursive(obj))
    

if __name__ == '__main__':
    ttr = I.unittest.TextTestRunner(tb_locals=True)
    I.unittest.main(testRunner=ttr, verbosity=2)

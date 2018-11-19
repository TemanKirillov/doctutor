#!/usr/bin/python3 

class I:
    'imported objects'
    import unittest
    import disp
    import obj

disp = I.disp.default()

class Test(I.unittest.TestCase):    
    def test(self):  
        obj = I.obj.Param('parameter', 'TYPE', repr('abc'), 'My parameter for test')
        print(disp(obj))

    def test_recurs(self):  
        obj1 = I.obj.Param('parameter1', 'TYPE', repr('abc'), 'My parameter for test')
        obj2 = I.obj.Param('parameter2', 'TYPE', repr('abc'), 'My parameter for test')
        obj3 = I.obj.Params((obj1, obj2))
        print(I.disp.recursive(obj3))

        obj4 = I.obj.Params((obj1, '<param2>'))
        print(I.disp.recursive(obj4))
        obj5 = I.obj.Params(('<param1>', '<param2>'))
        print(I.disp.recursive(obj5))

if __name__ == '__main__':
    ttr = I.unittest.TextTestRunner(tb_locals=True)
    I.unittest.main(testRunner=ttr, verbosity=2)

import unittest

from mydoc import in_builtins
from mydoc import add_tab
from mydoc import const
from mydoc import get_params
from mydoc import get_example
from mydoc import get_view_func
from mydoc import is_imp
from mydoc import get_view_attrs
from mydoc import get_view_class
from mydoc import get_view_module
from mydoc import method_to_operator
from mydoc import methods_to_operators
from mydoc import to_columns

class Test_in_builtins(unittest.TestCase):    
    
    def test_all(self):
        self.assertTrue(in_builtins(print))
        self.assertTrue(in_builtins(str))
        self.assertTrue(in_builtins(ValueError))
        self.assertFalse(in_builtins('string'))
        
class Test_add_tab(unittest.TestCase):    
    TEST1 = 'test\n\tstring\n'
    TEST2 = '\ttest\n\tstring'
    
    def test_all(self):    
        self.assertEqual(add_tab(self.TEST1), '\ttest\n\t\tstring\n')
        self.assertEqual(add_tab(self.TEST2), '\t\ttest\n\t\tstring')
        self.assertEqual(add_tab(self.TEST1, 2), '\t\ttest\n\t\t\tstring\n')



class Test_const(unittest.TestCase):    
    
    def test_all(self):    
        a = 1
        print('='*50)
        print('Обработка const:')
        print(const('a', repr(a)).expandtabs(4))
        
        print('Обработка const, как член модуля:')
        print(const('a', repr(a), 'name_module').expandtabs(4))
        
class Test_params(unittest.TestCase):    
    
    def test_all(self):    
        print('='*50)
        print('Обработка params:')
        import json
        print(get_params(json.dump))
        
        
class Test_example(unittest.TestCase):    
    
    def test_all(self):    
        print('='*50)
        print('Обработка get_example:')
        print(get_example(print).expandtabs(4))
        
class Test_get_view_func(unittest.TestCase):    
    
    def test_all(self):
        def test(a,b):
            pass
            
        print('='*50)
        print('Обработка встроенной функции:')
        print(get_view_func(print).expandtabs(4))
        
        print('='*50)
        print('Обработка пользовательской функции:')
        print(get_view_func(test).expandtabs(4))
        
class Test_is_imp(unittest.TestCase):    
    
    def test_all(self):    
        print('='*50)
        print('Обработка is_imp:')
        import inspect
        self.assertFalse(is_imp('CORO_CLOSED', inspect))
        self.assertFalse(is_imp('BlockFinder', inspect))
        self.assertFalse(is_imp('isbuiltin', inspect))
        self.assertTrue(is_imp('sys', inspect))
        self.assertTrue(is_imp('OrderedDict', inspect))
        self.assertTrue(is_imp('attrgetter', inspect))
        print('DONE')
        
class Test_get_view_attrs(unittest.TestCase):    
    
    def test_all(self):    
        print('='*50)
        print('Обработка get_view_attrs:')
        names = ['isabstract', 'CORO_CLOSED', 'ArgSpec']
        import inspect
        print(get_view_attrs(names, inspect).expandtabs(4))        

class Test_get_view_class(unittest.TestCase):    
    
    def test_all(self):
        import string
        import struct
    
        print('='*50)
        print('Обработка класса:')
        print(get_view_class(string.Template).expandtabs(4))
        print('='*50)
        print('Обработка ещё класса:')
        print(get_view_class(struct.Struct).expandtabs(4))
        import csv
        print('='*50)
        print('Обработка ещё класса:')
        print(get_view_class(csv.excel).expandtabs(4))
        
        from configparser import ConfigParser
        print('='*50)
        print(get_view_class(ConfigParser).expandtabs(4))
        
class Test_get_view_module(unittest.TestCase):    
    
    def test_all(self):
        import string
        print('='*50)
        print('Обработка модуля:')
        print(get_view_module(string).expandtabs(4))
        
        import binascii
        print('='*50)
        print('Обработка ещё модуля:')
        print(get_view_module(binascii).expandtabs(4))
        
        #import csv
        #print('='*50)
        #print('Ещё модуль (до кучи):')
        #print(get_view_module(csv).expandtabs(4))
        
        #import configparser
        #print('='*50)
        #print(get_view_module(configparser).expandtabs(4))
        
class Test_methods_to_operators(unittest.TestCase):    
    
    def test_all(self):  
        methods = dir(int)
        name_class = int.__name__
        text = to_columns(methods_to_operators(methods, name_class), 3)
        print(text)
        
class Test_to_columns(unittest.TestCase):    
    
    def test_all(self):  
    
        print('='*50)
        print('Test to_columns:')
        text = to_columns(range(100), 4)
        print(text)
        
        print('='*50)
        print('Test to_columns with empty arg:')
        text = to_columns([], 4)
        print(text)
        
class Test_partial(unittest.TestCase): #тестирование методов, образованных partialmethod
    
    def test_all(self):  
        
        from functools import partialmethod
        class Obj:
            def __init__(self):
                self.alive = False
            def set_state(self, state):
                self.alive = bool(state)

                
        class NewObj(Obj):
            set_alive = partialmethod(Obj.set_state, True)
            set_dead = partialmethod(Obj.set_state, False)
        
        print('='*50)
        print('Test method generated by partialmethod:')
        print(get_view_class(NewObj))
        print()
        print('='*50)
        print()
            

if __name__ == '__main__':
    ttr = unittest.TextTestRunner(tb_locals=True)
    
    unittest.main(testRunner=ttr, verbosity=2) 
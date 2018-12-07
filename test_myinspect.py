#!/usr/bin/python3 

class I:
    'imported objects'
    import unittest
    import string
    import pprint
    from myinspect import ownattr
    from myinspect import any_fullmatch
    from myinspect import getmembers
    from myinspect import isimp
    from myinspect import isinparent
    from myinspect import ContextPatterns
    from myinspect import getmembers_recursive
    from myinspect import isdunder
    from myinspect import getparent
    from myinspect import getparents
    from myinspect import attrs_by_parents
    from myinspect import mark_attrs

class Test_ownattr(I.unittest.TestCase):

    def test_builtin_func(self):
        gen = I.ownattr('hex', hex)
        lst = list(dict(gen))
        self.assertEqual(len(lst), 4)
        self.assertListEqual(lst, ['__class__', '__name__', '__qualname__', '__text_signature__'])

    def test_user_func(self):
        def test(a,b):
            ''' test function'''
        test.attr = 8
        lst = list(dict(I.ownattr('test', test)))
        self.assertEqual(len(lst), 6)
        self.assertListEqual(lst, ['__dict__', '__doc__', '__module__', '__name__', '__qualname__', 'attr'])

    def test_class(self):
        class Test:
            ''' test class'''
            a = 8
            def __init__(self):
                self.b = 22
            def method(self):
                pass

        lst = list(dict(I.ownattr('Test', Test)))
        self.assertEqual(len(lst), 7)
        self.assertListEqual(lst, ['__dict__', '__doc__', '__init__', '__module__', '__weakref__', 'a', 'method'])

        inst = Test()
        inst.attr = 'test attr'
        lst = list(dict(I.ownattr('Test', inst)))
        self.assertEqual(len(lst), 4)
        self.assertListEqual(lst, ['__class__', '__dict__', 'attr', 'b'])

    def test_module(self):
        lst = list(dict(I.ownattr('string', I.string)))
        self.assertEqual(len(lst), 22)
        self.assertListEqual(lst, ['Formatter', 'Template', '_TemplateMetaclass', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'ascii_letters', 'ascii_lowercase', 'ascii_uppercase', 'capwords', 'digits', 'hexdigits', 'octdigits', 'printable', 'punctuation', 'whitespace',] 
        )

class Test_any_fullmatch(I.unittest.TestCase):
    def test_all(self):
        patterns = ['a', '\d\d', '.+__']
        self.assertTrue(I.any_fullmatch('a', *patterns))
        self.assertTrue(I.any_fullmatch('23', *patterns))
        self.assertFalse(I.any_fullmatch('b', *patterns))
        self.assertFalse(I.any_fullmatch('235', *patterns))

class Test_getmembers(I.unittest.TestCase):
    def test_isimp(self):
        lst = list(dict(I.getmembers('string', I.string, I.isimp)))
        self.assertListEqual(lst, ['_ChainMap','_re', '_string' ] )

class Test_ContextPatterns(I.unittest.TestCase):
    def test_sn(self):
        def f1():
            pass
        f1.a25 = 3
        with I.ContextPatterns(r'a\d\d', r'__\w\w') as context:
            func = context.match_nameattr
            self.assertTrue(func('f1', f1, 'a25'))
            self.assertFalse(func('f1', f1, 'abc'))
            self.assertTrue(func('f1', f1, '__ab'))
            self.assertFalse(func('f1', f1, '__ab__'))

    def test_sn_getmembers(self):
        def f1():
            pass
        f1.a25 = 3
        f1.abc = 3
        f1.__ab = 3
        f1.__ab__ = 3
        with I.ContextPatterns(r'a\d\d', r'__\w\w') as context:
            gen = I.getmembers('f1', f1, context.match_nameattr)
            self.assertListEqual(list(gen), [('a25', 3)])

    def test_qn(self):
        def f1():
            pass
        f1.a25 = 3
        with I.ContextPatterns(r'f1[.]a\d\d', r'f2[.]__\w\w') as context:
            func = context.match_qualname
            self.assertTrue(func('f1', f1, 'a25'))
            self.assertFalse(func('f1', f1, 'abc'))
            self.assertFalse(func('f1', f1, '__ab'))
            self.assertTrue(func('f2', f1, '__ab'))

class Test_getmembers_recursive(I.unittest.TestCase):
    
    def test_isimp(self):
        # извлечение импортированных элементов рекурсивно
        def temp(name, obj, nameattr): #чтобы избежать зацикливания на внутренних атрибутах
            return I.isimp(name, obj, nameattr) and not I.isdunder(name, obj, nameattr)
        def all_(*args):
            return True
        gen = I.getmembers_recursive('string', I.string, temp, all_ ) 
        st = set(dict(gen))
        self.assertEqual(len(st), 32)
        example = {'string._ChainMap', 'string._re', 'string._re._locale', 'string._re._locale.Error', 'string._re._pattern_type', 'string._re.copyreg', 'string._re.enum', 'string._re.enum.DynamicClassAttribute', 'string._re.enum.MappingProxyType', 'string._re.enum.OrderedDict', 'string._re.enum._or_', 'string._re.enum.reduce', 'string._re.enum.sys', 'string._re.enum.sys.excepthook', 'string._re.error', 'string._re.functools', 'string._re.functools.MappingProxyType', 'string._re.functools.RLock', 'string._re.functools.WeakKeyDictionary', 'string._re.functools.cmp_to_key', 'string._re.functools.get_cache_token', 'string._re.functools.namedtuple', 'string._re.functools.recursive_repr', 'string._re.functools.reduce', 'string._re.sre_compile', 'string._re.sre_compile._sre', 'string._re.sre_compile.error', 'string._re.sre_compile.sre_parse', 'string._re.sre_compile.sre_parse.error', 'string._re.sre_parse', 'string._re.sre_parse.error', 'string._string',}
        self.assertSetEqual(example, st)

    def test_ownattr(self):
        #тестирование извлечения собственных аргументов 
        def temp(*args):
            return I.isimp(*args) or I.isdunder(*args) or I.isinparent(*args)

        def temp_not(*args):
            return not temp(*args)

        def all_(*args):
            return True
        def not_parent(*args):
            return not I.isinparent(*args)
        
        gen = I.getmembers_recursive('string', I.string, not_parent, temp_not ) 
        lst = list(gen)
        self.assertEqual(len(lst), 178)
        # print('Вывод собственных аргументов модуля string рекурсивно')
        # [print(i[0]) for i in lst]

class Test_getparent(I.unittest.TestCase):
    
    def test(self):
        class A:
            a = 1
        class B(A):
            b = 1
        C = B()
        C.a = 2
        self.assertIs(I.getparent(C, 'a'), C)
        self.assertIs(I.getparent(B, 'a'), A)
        self.assertIs(I.getparent(B, 'b'), B)
        self.assertIs(I.getparent(B, '__hash__'), object)
        with self.assertRaises(AttributeError):
            I.getparent(C, 'd')

class Test_getparents(I.unittest.TestCase):
    def test(self):
        class A:
            a = 1
        class B(A):
            b = 1
        C = B()
        C.a = 2
        self.assertEqual(I.getparents(C), (C, B, A, object))
        self.assertEqual(I.getparents(B), (B, A, object))
        self.assertEqual(I.getparents(hex), (hex, hex.__class__, object))
        self.assertEqual(I.getparents(object), (object,))
        self.assertEqual(I.getparents(type), (type, object,))

class Test_attrs_by_parents(I.unittest.TestCase):
    def test(self):
        class A:
            a = 1
        class B(A):
            b = 1
        C = B()
        C.a = 2
        dct = I.attrs_by_parents(C)
        key_C = repr(C)
        key_A = repr(A)
        self.assertEqual(dct[key_C]['a'], 2)
        self.assertEqual(dct[key_A]['__weakref__'], None)

class Test_mark_attrs(I.unittest.TestCase):
    def test(self):
        class A:
            a = 1
        class B(A):
            b = 1
        C = B()
        C.a = 2
        import string
        C.string = string 
        dct = I.mark_attrs(C)
        self.assertTrue(dct['__le__'].Is('parent'))
        self.assertTrue(dct['__le__'].Is('magic'))
        self.assertTrue(dct['__le__'].Is('internal'))
        self.assertTrue(dct['__le__'].Is('nonimported'))
        self.assertTrue(dct['a'].Is('nonparent'))
        self.assertTrue(dct['string'].Is('imported'))

if __name__ == '__main__':
    ttr = I.unittest.TextTestRunner(tb_locals=True)
    I.unittest.main(testRunner=ttr, verbosity=2)

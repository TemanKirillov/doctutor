#!/usr/bin/python3 
''' Экземпляры могут иметь такие методы, которых не имеет класс.
    '''
class I:
    from dispatcher import Dispatcher
    from collections import namedtuple
    from inspect import getdoc
    import inspect
    import collections

def is_dunder(attr):
    name, obj = attr
    if name.startswith('__') and name.endswith('__'):
        return True
    else:
        return False

def getdunder(object):
    for name, obj in inspect.getmembers(object):
        if name.startswith('__') and name.endswith('__'):
            yield name, obj

def getnondunder(object):
    for name, obj in inspect.getmembers(object):
        if not (name.startswith('__') and name.endswith('__')):
            yield name, obj

def getdoc(obj):
    if obj is type:
        return I.inspect.getdoc(obj)
    doc_obj = I.inspect.getdoc(obj)
    doc_cls = I.inspect.getdoc(obj.__class__)
    if doc_obj == doc_cls:
        return ''
    else:
        return doc_obj

def is_dunder(name):
    if name.startswith('__') and name.endswith('__'):
        return True
    else:
        return False

def getmembers(name, obj, blacklist, asdata, delnames):
    ''' Генератор. Рекурсивно выталкивает кортежи (квалифицированное имя, объект) из объектов и его атрибутов. Выводит имена, которые определены только в этом объекте. Не для всех объектов это определить легко, поэтому для тонкой настройки используются параметры asdata и delnames. 
    blacklist: iterable не квалифицированные имена объектов, которые не выводятся. 
    asdata: iterable принимает квалифицированные имена объектов, для которых не нужно рекурсивно обходить атрибуты
    delnames: iterable принимает квалифицированные имена объектов, которые не нужно выводить вовсе '''

    # Сначала всегда выводится сам объект, как данные
    yield name, obj

    if blacklist is None:
        blacklist = []
    if asdata is None:
        asdata = []
    if delnames is None:
        delnames = []

    if name in asdata:
        return 
    elif I.inspect.ismodule(obj):
        members = myattr_module(obj, blacklist)
    else:
        members = myattr(obj, blacklist)

    for namemem, objmem in members:
        qualname = '.'.join([name, namemem])
        if qualname in delnames:
            pass
        elif is_dunder(namemem): #никогда не получать атрибуты от __dunder__
            yield qualname, objmem
        else:
            yield from getmembers(qualname, objmem, blacklist, asdata, delnames)

def extract_names(name, obj, names):
    gen = getmembers(name, obj)
    for namemem, objmem in gen:
        short = namemem.split('.')[-1]
        if short in names: 
            yield namemem, objmem

def extract_comments(name, obj):
    gen = getmembers(name, obj)
    for namemem, objmem in gen:
        comment = I.inspect.getcomments(objmem)
        yield namemem, comment


def is_descriptor(obj):
    if hasattr(obj, '__get__') or hasattr(obj, '__set__'):
        return True
    return False

def myattr(obj, blacklist=None):
    if blacklist is None:
        blacklist = []
    memobj = I.inspect.getmembers(obj)
    memcls = I.collections.OrderedDict(I.inspect.getmembers(obj.__class__))
    for namemem, objmem in memobj:
        if namemem in blacklist:
            continue
        if namemem in memcls:
            parent_obj = memcls[namemem]
            if (parent_obj == objmem or is_descriptor(parent_obj)):
                pass
            else:
                yield namemem, objmem
        else:
            yield namemem, objmem

def myattr_module(module, blacklist=None):
    ''' Атрибуты модуля, исключая импортированные '''
    for name, obj in myattr(module, blacklist):
        modattr = I.inspect.getmodule(obj)
        if modattr is module or modattr is None:
            yield name, obj


def test():
    def test_myattr():
        gen = myattr(hex)
        lst = list(gen)
        print(len(lst))
        [print(i) for i in lst]

        def test(a,b):
            ''' test function'''
        test.attr = 8
        lst = list(myattr(test))
        print(len(lst))
        [print(i) for i in lst]

        class Test:
            ''' test class'''
            a = 8
            def __init__(self):
                self.b = 22
            def method(self):
                pass

        lst = list(myattr(Test))
        print(len(lst))
        [print(i) for i in lst]

        inst = Test()
        lst = list(myattr(inst))
        print(len(lst))
        [print(i) for i in lst]
        print(inst.__subclasshook__ is Test.__subclasshook__)

        import string as inst
        lst = list(myattr(inst))
        print(len(lst))
        [print(i[0]) for i in lst]

    test_myattr()

    def test_myattr_module():
        import string
        gen = myattr_module(string)
        lst = list(gen)
        print(len(lst))
        [print(i[0]) for i in lst]

    test_myattr_module()

    def test_getmembers():
        import string
        gen = getmembers('string', string)
        lst = list(gen)
        print(len(lst))
        [print(i) for i in lst]

    test_getmembers()

def test2():
    import string
    blacklist = [
                 '__dict__',
                 '__name__',
                 '__qualname__',
                 '__module__',
                 '__weakref__',
                ]

    asdata = [#'string.Template.flags',
              ]

    delnames = ['string.__builtins__',
                'string.Template.flags.bit_length',
                'string.Template.flags.conjugate',
                'string.Template.flags.denominator',
                'string.Template.flags.from_bytes',
                'string.Template.flags.imag',
                'string.Template.flags.name',
                'string.Template.flags.numerator',
                'string.Template.flags.real',
                'string.Template.flags.to_bytes',
                'string.Template.flags.value',

               ]
    gen = getmembers('string', string, blacklist, asdata, delnames)
    print('\n' * 5)
    _ = [print(i) for i in gen]


    

#test()
test2()

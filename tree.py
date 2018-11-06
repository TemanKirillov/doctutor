#!/usr/bin/python3 
'''
Функции для формирования дерева объектов для документации
'''

class I:
    import inspect
    from dispatcher import Dispatcher
    import re


def to_short(qualname):
    ''' Преобразовать квалифицированное имя в короткое.''' 
    short = qualname.split('.')[-1]
    return short

def any_fullmatch(string, *patterns):
    ''' Вернёт True, если совпало хотя бы с одним из шаблонов полностью.'''
    gen = (I.re.fullmatch(pattern, string) for pattern in patterns)
    return any(gen)

def isdescriptor(obj):
    ''' Реализован ли в объекте протокол дескриптора?'''
    if hasattr(obj, '__get__') or hasattr(obj, '__set__'):
        return True
    return False

ownattr = I.Dispatcher() #Диспетчер для извлечения атрибутов из объекта

@ownattr.bind_default
def ownattr_object(obj):
    ''' Генераторная функция. Производит атрибуты объекта в стиле inspect.getmembers, которые принадлежат самому объекту. '''

    memobj = I.inspect.getmembers(obj)
    cls = obj.__class__
    memcls = dict(I.inspect.getmembers(cls))

    for namemem, objmem in memobj:
        if namemem in memcls:
            parent_obj = memcls[namemem]
            if (parent_obj == objmem or isdescriptor(parent_obj)):
                pass
            else:
                yield namemem, objmem
        else:
            yield namemem, objmem

@ownattr.bind(I.inspect.ismodule)
def ownattr_module(module):
    ''' Генераторная функция. Производит атрибуты модуля, исключая импортированные '''
    for name, obj in ownattr_object(module):
        modattr = I.inspect.getmodule(obj)
        if modattr is module or modattr is None:
            yield name, obj

if __name__ == '__main__':
    pass

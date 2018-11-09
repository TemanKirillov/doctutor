#!/usr/bin/python3 
'''
Функции для формирования дерева объектов для документации
'''

class I:
    import inspect
    import re

def to_short(qualname):
    ''' Преобразовать квалифицированное имя в короткое.''' 
    short = qualname.split('.')[-1]
    return short

def any_fullmatch(string, *patterns):
    ''' Вернёт True, если совпало хотя бы с одним из шаблонов полностью.'''
    gen = (I.re.fullmatch(pattern, string) for pattern in patterns)
    return any(gen)

def getfunc_match_sn(*patterns):
    'Возвращает функцию, которая возвращает True, если имя атрибута совпало с одним из указанных паттернов'
    def ismatching_shortname(name, obj, nameattr):
        return any_fullmatch(nameattr, *patterns)
    return ismatching_shortname

def getfunc_match_qn(*patterns):
    'Возвращает функцию, которая возвращает True, если квалифицированное имя name.nameattr атрибута совпало с одним из указанных паттернов'
    def ismatching_qualname(name, obj, nameattr):
        qualname = '.'.join([name, nameattr])
        return any_fullmatch(qualname, *patterns)
    return ismatching_qualname

def getmembers_recursive(name, obj, predicate):
    ''' Генераторная функция. Реализует рекурсивный обход атрибутов объекта. '''

def isdescriptor(obj):
    ''' Реализован ли в объекте протокол дескриптора?'''
    if hasattr(obj, '__get__') or hasattr(obj, '__set__'):
        return True
    return False

def isinparent(name, obj, nameattr):
    ''' Наследован ли атрибут от родителя.
        Принимает объект и имя его атрибута'''
    cls = obj.__class__
    objattr = getattr(obj, nameattr)
    memcls = dict(I.inspect.getmembers(cls))

    if nameattr in memcls:
        parent_obj = memcls[nameattr]
        if (parent_obj == objattr or isdescriptor(parent_obj)):
            return True
    return False

def isimp(name, obj, nameattr):
    ''' Импортирован ли атрибут?
        Принимает объект и имя его атрибута'''
    objattr = getattr(obj, nameattr)
    module = I.inspect.getmodule(obj)
    modattr = I.inspect.getmodule(objattr)
    if modattr is module or modattr is None:
        return False
    else:
        if I.inspect.isroutine(objattr) or I.inspect.isclass(objattr) or I.inspect.ismodule(objattr):
            return True
        else:
            return False
    

def ownattr(name, obj):
    ''' Генераторная функция. Производит атрибуты объекта в стиле inspect.getmembers, которые принадлежат самому объекту. '''

    memobj = I.inspect.getmembers(obj)

    for namemem, objmem in memobj:
        if isinparent(name, obj, namemem) or isimp(name, obj, namemem):
            pass
        else:
            yield namemem, objmem

def getmembers(name, obj, predicate):
    ''' Генератор. Реализует другой тип предиката для inspect.getmembers. Рекурсивно выталкивает кортежи (имя, объект) из объектов и его атрибутов.
        predicate - функция с сигнатурой (obj, nameattr): принимает объект и имя его атрибута. Возвращает True, если атрибут должен быть вытолкнут. ''' 

    members = I.inspect.getmembers(obj)

    for namemem, objmem in members:
        if predicate(name, obj, namemem):
            yield namemem, objmem

if __name__ == '__main__':
    pass

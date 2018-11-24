#!/usr/bin/python3 
'''
Функции для формирования дерева объектов для документации
'''

class I:
    import inspect
    import re
    from contextlib import AbstractContextManager

class AttributeException:
    'Класс для представления атрибута, обращаясь к которому возникает исключение'
    def __init__(self, exc):
        self.exc = exc
    def __repr__(self):
        namecls = self.__class__.__name__
        return '{cls}({exc})'.format(namecls,self.exc) 
    @classmethod
    def make(cls, obj, nameattr):
        try:
            objattr = getattr(obj, nameattr)
        except Exception as e:
            return cls(e)

def to_short(qualname):
    ''' Преобразовать квалифицированное имя в короткое.''' 
    short = qualname.split('.')[-1]
    return short

def any_fullmatch(string, *patterns):
    ''' Вернёт True, если совпало хотя бы с одним из шаблонов полностью.'''
    gen = (I.re.fullmatch(pattern, string) for pattern in patterns)
    return any(gen)

class ContextPatterns(I.AbstractContextManager):
    def __init__(self, *patterns):
        self.patterns = patterns

    def __exit__(self, *exc):
        pass

    def match_nameattr(self, name, obj, nameattr):
        'возвращает True, если имя атрибута совпало с одним из указанных паттернов'
        return any_fullmatch(nameattr, *self.patterns)

    def match_qualname(self, name, obj, nameattr):
        'возвращает True, если квалифицированное имя name.nameattr атрибута совпало с одним из указанных паттернов'
        qualname = '.'.join([name, nameattr])
        return any_fullmatch(qualname, *self.patterns)

def getmembers_recursive(name, obj, predicate, predicate_recursive):
    ''' Генераторная функция. Реализует рекурсивный обход атрибутов объекта. 
    name: имя объекта,
    obj: сам объект,
    predicate: как в функции getmembers
    predicate_recursive: функция-предикат, должна возвращать True, если атрибуты этого атрибута должны быть также обойдены'''
    for nameattr, objattr in getmembers(name, obj, predicate):
        qualname= '.'.join([name, nameattr])
        yield qualname, objattr
        if predicate_recursive(name, obj, nameattr):
            yield from getmembers_recursive(qualname, objattr, predicate, predicate_recursive)

def isdescriptor(obj):
    ''' Реализован ли в объекте протокол дескриптора?'''
    if hasattr(obj, '__get__') or hasattr(obj, '__set__'):
        return True
    return False

def isdunder(name, obj, nameattr):
    return any_fullmatch(nameattr, r'__\w+__')

def isinparent(name, obj, nameattr):
    ''' Наследован ли атрибут от родителя.
        Принимает объект и имя его атрибута'''
    if getparent(obj, nameattr) is obj:
        return False
    else:
        return True

def getparent(obj, nameattr):
    ''' Возвращает объект, в котором определён атрибут nameattr объекта obj'''
    if I.inspect.isclass(obj):
        loc = I.inspect.classify_class_attrs(obj)
        memcls = {attr.name: attr for attr in loc}
        if nameattr in memcls:
            return memcls[nameattr].defining_class
        else:
            raise AttributeError('Object {!r} has no attribute {!r}'.format(obj, nameattr))
    else:
        cls = obj.__class__
        objattr = getattr(obj, nameattr)
        memcls = dict(I.inspect.getmembers(cls))

        if nameattr in memcls:
            parent_obj = memcls[nameattr]
            if (parent_obj == objattr or isdescriptor(parent_obj)):
                return getparent(cls, nameattr)
            else:
                return obj #атрибут переопределён в экземпляре
        return obj #атрибут определён в экземпляре

def isimp(name, obj, nameattr):
    ''' Импортирован ли атрибут?
        Принимает объект и имя его атрибута'''
    if isinparent(name, obj, nameattr):
        return False
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
    
def isattrexception(name, obj, nameattr):
    try:
        objattr = getattr(obj, nameattr)
    except Exception as e:
        return True
    return False

def getattr(obj, nameattr):
    ''' Реализация getattr для работы с атрибутами, которые возбуждают AttributeError при обращении к себе. '''
    dct = dict(I.inspect.getmembers(obj))
    if nameattr in dct:
        return dct[nameattr]
    raise AttributeError('Object {!r} has no attribute {!r}'.format(obj, nameattr))

def ownattr(name, obj):
    ''' Генераторная функция. Производит атрибуты объекта в стиле inspect.getmembers, которые принадлежат самому объекту. '''

    memobj = I.inspect.getmembers(obj)

    for namemem, objmem in memobj:
        if isinparent(name, obj, namemem) or isimp(name, obj, namemem):
            pass
        else:
            yield namemem, objmem

def getmembers(name, obj, predicate):
    ''' Генератор. Реализует другой тип предиката для inspect.getmembers. Выталкивает кортежи (имя, объект) из объектов и его атрибутов.
        predicate - функция с сигнатурой (name, obj, nameattr): принимает имя объекта, объект и имя его атрибута. Возвращает True, если атрибут должен быть вытолкнут. ''' 

    members = I.inspect.getmembers(obj)

    for namemem, objmem in members:
        if predicate(name, obj, namemem):
            yield namemem, objmem

if __name__ == '__main__':
    pass

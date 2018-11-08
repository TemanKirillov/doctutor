#!/usr/bin/python3 
'''
Функции для формирования дерева объектов для документации
'''

class I:
    import inspect

def isdescriptor(obj):
    ''' Реализован ли в объекте протокол дескриптора?'''
    if hasattr(obj, '__get__') or hasattr(obj, '__set__'):
        return True
    return False


def isinparent(obj, nameattr):
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

def ownattr(obj):
    ''' Генераторная функция. Производит атрибуты объекта в стиле inspect.getmembers, которые принадлежат самому объекту. '''

    memobj = I.inspect.getmembers(obj)

    for namemem, objmem in memobj:
        if isinparent(obj, namemem):
            pass
        else:
            yield namemem, objmem

if __name__ == '__main__':
    pass

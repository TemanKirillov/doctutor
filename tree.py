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

def ownattr(obj):
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

if __name__ == '__main__':
    pass

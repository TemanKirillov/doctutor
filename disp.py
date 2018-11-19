#!/usr/bin/python3 
# -*- coding: utf-8 -*-

''' Объекты диспетчеризации для представления объектов модуля obj.py модулем repr.py '''

class I:
    from functools import singledispatch
    import repr
    import obj

def construct_dispatch(objs, reprobj):
    ''' Строит диспетчер для объектов objs с использованием методов объекта reprobj (repr.Repr). '''
    disp = I.singledispatch(reprobj.Default)
    for obj in objs:
        name = obj.__name__
        if hasattr(reprobj, name):
            method = getattr(reprobj, name)
            disp.register(obj, method)
        else:
            msg = "Not possible to register {}".format(name)
            raise ValueError(msg)
    return disp

def default():
    ''' Диспетчер объектов по умолчанию. '''
    objs = [ getattr(I.obj, name) for name in I.obj.__all__]
    disp = construct_dispatch(objs, I.repr.Repr())
    return disp

def recursive(obj):
    ''' Рекурсивно обходит объект, отправляя вложенные объекты на представление'''
    disp = default()
    loc_isinstance = lambda obj: isinstance(obj, I.obj.Obj)
    if loc_isinstance: # если это объект для представления
        if any(map(loc_isinstance, obj)): # если есть вложенные объекты для представления
            cls = obj.__class__
            iterable = []
            for item in obj:
                if loc_isinstance(item):
                    iterable.append(recursive(item))
                else:
                    iterable.append(item)
            return disp(cls(iterable))

    return disp(obj)

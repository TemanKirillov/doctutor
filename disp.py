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



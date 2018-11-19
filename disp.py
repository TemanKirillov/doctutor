#!/usr/bin/python3 
# -*- coding: utf-8 -*-

''' Объекты диспетчеризации для представления объектов модуля obj.py модулем repr.py '''

class I:
    from functools import singledispatch

def construct_dispatch(objs, reprobj):
    disp = I.singledispatch(reprobj.Default)
    for obj in objs:
        name = obj.__name__
        if hasattr(reprobj, name):
            method = getattr(reprobj, name)
            disp.register(obj, method)
        else:
            msg = "Not possible to register {}".format(name)
            raise ValueError(msg)



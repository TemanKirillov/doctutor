#!/usr/bin/python3 
# -*- coding: utf-8 -*-
''' Конструкторы объектов для представления из реальных. '''

class I:
    import inspect
    import obj
    from mycollections import DictAttr

class Make:
    def Parents(self, obj):
        try:
            return I.obj.Parents(repr(item) for item in I.inspect.getmro(obj)[1:])
        except AttributeError:
            return I.obj.Parents()

#!/usr/bin/python3 
# -*- coding: utf-8 -*-
''' Конструкторы объектов для представления из реальных. '''

class I:
    import inspect
    import obj

class Make:
    def Params(self, obj):
        res = list()
        sign = I.inspect.signature(obj)
        for name, param in sign.parameters.items():
            kind = str(param.kind)
            if param.default == I.inspect._empty:
                default = ''
            else:
                default = str(param.default)
            if param.annotation == I.inspect._empty:
                anno = ''
            else:
                anno = str(param.annotation)
            res.append(I.obj.Param(name, kind, default, anno))
        return I.obj.Params(res)

    


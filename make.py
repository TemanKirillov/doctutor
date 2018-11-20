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
                default = repr(param.default)
            if param.annotation == I.inspect._empty:
                anno = ''
            else:
                anno = str(param.annotation)
            res.append(I.obj.Param(name, kind, default, anno))
        return I.obj.Params(res)
    
    def Return(self, obj):
        sign = I.inspect.signature(obj)
        if sign.return_annotation == I.inspect._empty:
            res = ''
        else:
            res = repr(sign.return_annotation)
        return I.obj.Return(res)
        
    


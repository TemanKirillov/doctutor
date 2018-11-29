#!/usr/bin/python3 
# -*- coding: utf-8 -*-
''' Конструкторы объектов для представления из реальных. '''

class I:
    import inspect
    import obj
    from mycollections import DictAttr

class Make:
    def Params(self, obj):
        params = I.obj.Params()
        sign = I.inspect.signature(obj)
        for name, param in sign.parameters.items():
            res = I.obj.Param()
            res.name = name
            res.kind = str(param.kind)
            if param.default != I.inspect._empty:
                res.default = repr(param.default)
            if param.annotation != I.inspect._empty:
                res.desc = str(param.annotation)
            params[name] = res
        return params
    
    def Return(self, obj):
        res = I.obj.Return()
        sign = I.inspect.signature(obj)
        if sign.return_annotation != I.inspect._empty:
            res.desc = repr(sign.return_annotation)
        return res

    def Func(self, obj):
        res = I.obj.Func()
        res.name = obj.__name__
        res.sign = str(I.inspect.signature(obj))
        res.doc = I.inspect.getdoc(obj)
        res.params = self.Params(obj)
        res.return_ = self.Return(obj)
        return res
        


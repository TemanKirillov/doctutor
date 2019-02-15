#!/usr/bin/python3 
# -*- coding: utf-8 -*-
''' Конструкторы объектов для представления из реальных. '''

class I:
    import inspect
    from collections import OrderedDict
    import obj
    from mycollections import DictAttr
    import myinspect

class Make:
    def Params(self, obj):
        res = I.OrderedDict()
        res['type'] = 'Params'
        res['content'] = I.OrderedDict()
        rc = res['content']
        sign = I.inspect.signature(obj)
        for name, param in sign.parameters.items():
            prm = I.OrderedDict()
            prm['type'] = 'Param'
            prm['content'] = I.OrderedDict()
            pc = prm['content']
            pc['name'] = name
            pc['kind'] = str(param.kind)
            if param.default != I.inspect._empty:
                pc['default'] = repr(param.default)
            else:
                pc['default'] = ''
            if param.annotation != I.inspect._empty:
                pc['desc'] = str(param.annotation)
            else:
                pc['desc'] = ''
            rc[name] = prm
        return res
    
    def Return(self, obj):
        res = I.OrderedDict()
        res['type'] = 'Return'

        sign = I.inspect.signature(obj)
        if sign.return_annotation != I.inspect._empty:
            res['content'] = repr(sign.return_annotation)
        else:
            res['content'] = ''
        return res


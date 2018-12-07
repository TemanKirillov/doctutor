#!/usr/bin/python3 
# -*- coding: utf-8 -*-
''' Конструкторы объектов для представления из реальных. '''

class I:
    import inspect
    import obj
    from mycollections import DictAttr
    import myinspect

class Make:
    def Params(self, obj):
        params = I.obj.Params()
        sign = I.inspect.signature(obj)
        for name, param in sign.parameters.items():
            res = I.obj.Param()
            res._.name = name
            res._.kind = str(param.kind)
            if param.default != I.inspect._empty:
                res._.default = repr(param.default)
            if param.annotation != I.inspect._empty:
                res._.desc = str(param.annotation)
            params[name] = res
        return params
    
    def Return(self, obj):
        res = I.obj.Return()
        sign = I.inspect.signature(obj)
        if sign.return_annotation != I.inspect._empty:
            res._.desc = repr(sign.return_annotation)
        return res

    def Func(self, obj):
        res = I.obj.Func()
        res._.name = obj.__name__
        res._.sign = str(I.inspect.signature(obj))
        res._.doc = I.inspect.getdoc(obj)
        res._.params = self.Params(obj)
        res._.return_ = self.Return(obj)
        return res

    def Attrs(self, obj):
        members = I.inspect.getmembers(obj)
        return I.obj.Attrs(members)

    def AttrsAll(self, obj):
        res = I.obj.AttrsAll()
        res['own'] = I.obj.OwnAttrs()
        res['internal'] = I.obj.InternalAttrs()
        res['import'] = I.obj.ImportedAttrs()
        dct = I.myinspect.mark_attrs(obj)
        parents = I.myinspect.getparents(obj)[1:] #без самого объекта
        for name, marked in dct.items():
            if marked.Is('nonmagic'):
                if marked.Is('parent'):
                    pass #наследованные
                elif marked.Is('imported'):
                    res['import'][name] = marked.o
                elif marked.Is('internal'):
                    res['internal'][name] = marked.o
                else:
                    res['own'][name] = marked.o
                
            else:
                continue
        return res



        
    def ImportedAttrs(self, obj):
        members = I.myinspect.getmembers('', obj, I.myinspect.isimp)
        return I.obj.ImportedAttrs(members)
        


#!/usr/bin/python3 
# -*- coding: utf-8 -*-

''' Объекты для представления модулем repr. '''

__all__ = ['Attrs', 'BlockOperators', 'Class', 'Example', 'Except', 'Exceptions', 'Func', 'GroupAttrs', 'GroupOperators', 'Module', 'Operators', 'Param', 'Params', 'Parents', 'Return']

class I:
    from collections import namedtuple
    from collections import UserList
    from mycollections import DictAttr
    from itertools import repeat

class Obj(I.DictAttr):
    ''' Базовый класс всех объектов модуля'''
    _fields = ()

    def __init__(self, *args, **kwargs):
        self._type = self.__class__.__name__
        self.update(zip(self._fields, I.repeat('')))
        super().__init__(*args, **kwargs)

    @classmethod
    def from_iterable(cls, iterable):
        instance = cls()
        instance.update(zip(cls._fields, iterable))
        return instance

    def __iter__(self):
        elements = iter(self.values())
        _ = next(elements) #ignore self._type
        return elements
        
class Param(Obj):
    ''' Класс представления информации о параметре функции. '''
    _fields = ('name', 'kind', 'default', 'desc')

class Params(Obj):
    ''' Класс представления параметров'''

class Return(Obj):
    ''' Класс представления информации о возвращаемом значении. '''
    _fields = ('desc',)

class Func(Obj):
    ''' Класс представления информации о функции. '''
    _fields = ('name', 'sign', 'doc', 'params', 'return_', 'example', 'exceptions')
    


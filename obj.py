#!/usr/bin/python3 
# -*- coding: utf-8 -*-

''' Объекты для представления модулем repr. '''

__all__ = ['Attrs', 'Block', 'Func', 'GroupAttrs', 'Named', 'Param', 'Params', 'Return']

class I:
    from collections import namedtuple
    from collections import UserList
    from mycollections import DictAttr
    from itertools import repeat

class Obj(I.DictAttr):
    ''' Базовый класс всех объектов модуля'''
    _fields = ()

    def __init__(self, *args, **kwargs):
        self.update(zip(self._fields, I.repeat(''))) #сначала нужно заполнить пустыми значениями
        super().__init__(*args, **kwargs)
        self._._type = self.__class__.__name__

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

class Attrs(Obj):
    ''' Класс представления последовательности атрибутов'''

class Named(Obj):
    ''' Класс чего-то именованного. '''
    _fields = ('name', 'content')
    
class Block(Obj):
    ''' Класс блока. Имя, описание и содержимое блока.'''
    _fields = ('name', 'desc', 'content')

class GroupAttrs(Named):
    ''' Класс атрибутов и имени группы, в которую они входят'''


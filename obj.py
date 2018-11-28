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
        
class Param(Obj):
    ''' Класс представления информации о параметре функции. '''
    _fields = ('name', 'kind', 'default', 'desc')

class Params(Obj):
    ''' Класс представления параметров'''

class Return(I.namedtuple('_Return', 'desc'), Obj):
    ''' Класс представления информации о возвращаемом значении. '''

class Example(I.namedtuple('_Example', 'desc'), Obj):
    ''' Класс представления информации с текстом примера. '''

class Except(I.namedtuple('_Except', 'name desc example'), Obj):
    ''' Класс представления информации об исключении. '''

class Exceptions(I.UserList, Obj):
    ''' Класс представления исключений'''

class Func(I.namedtuple('_Func', 'name sign doc params return_ example exceptions'), Obj):
    ''' Класс представления информации о функции. '''

class Parents(I.UserList, Obj):
    ''' Класс представления родителей класса'''

class BlockOperators(I.UserList, Obj):
    ''' Класс последовательности операторов'''

class GroupOperators(I.namedtuple('_GroupOperators', 'owner operators'), Obj):
    ''' Класс операторов и их класса-владельца'''

class Operators(I.UserList, Obj):
    ''' Класс последовательности групп операторов класса'''

class Attrs(I.UserList, Obj):
    ''' Класс представления последовательности атрибутов'''

class GroupAttrs(I.namedtuple('_GroupAttrs', 'name attrs'), Obj):
    ''' Класс атрибутов и имени группы, в которую они входят'''

class Class(I.namedtuple('_Class', 'name doc parents init operators attrs'), Obj):
    ''' Класс представления информации о классе. '''
	
class Module(I.namedtuple('_Module', 'name doc attrs'), Obj):
    ''' Класс представления информации о модуле. '''

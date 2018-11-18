#!/usr/bin/python3 

''' Объекты для представления модулем repr. '''

class I:
    from collections import namedtuple

class Param(I.namedtuple('_Param', 'name kind default desc')):
    ''' Класс представления информации о параметре функции. '''

class Func(I.namedtuple('_Func', 'name sign doc params return_ example exceptions'):
    ''' Класс представления информации о функции. '''

class Class(I.namedtuple('_Class', 'name doc parents init operators attrs'):
    ''' Класс представления информации о классе. '''
	
class Default(I.namedtuple('_Default', 'name value doc'):
    ''' Класс представления объекта по умолчанию. '''

class Module(I.namedtuple('_Module', 'name doc attrs'):
    ''' Класс представления информации о модуле. '''

class Operators(I.namedtuple('_Operators', 'cls operators'):
    ''' Класс представления информации о операторах.
        cls: имя класса, в котором определены операторы,
        operators: iterable с именами операторов'''

class GroupAttrs(I.namedtuple('_GroupAttrs', 'name attrs'):
    ''' Класс представления информации о группе атрибутов. 
        name: имя группы,
        attrs: iterable of str, каждая str с описанием одного атрибута'''

class Except(I.namedtuple('_Except', 'name desc example')):
    ''' Класс представления информации об исключении. '''



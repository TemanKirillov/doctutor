#!/usr/bin/python3 
''' Модуль представления объектов в строковом виде.'''

class I:
    from itertools import zip_longest
    from math import ceil

class Repr:
    ''' Класс предоставления информации об объектах'''

    DESC_DEFAULT = 'Описание отсутствует'
    PARAMS = 'Параметры'
    NONE = '--НЕТ--'
    NO_INFO = 'Информации нет'
    RETURN = 'Возвращаемое значение'
    EXAMPLE = 'Пример'
    EXCEPTIONS = 'Исключения'
    PARENTS = 'Предки'
    OPERATORS = 'Поддержка операторов и протоколов'
    OPERATORS_OWN = 'Собственная реализация'
    OPERATORS_PARENT = 'Наследована от'
    
    def Example(self, obj):
        ''' Возвращает отформатированный текст примера'''
        desc, = obj
        res = '\n'.join((self.EXAMPLE, add_tab(desc)))
        return res

    def Except(self, obj): 
        ''' Представление экземпляра mydoc.Except'''
        #поля name desc example
        name, desc, example, = obj
        res = []
        res.append(name)
        if desc:
            res.append(add_tab(desc))
        res.append(add_tab(example))
        res = '\n'.join(res)
        return res

    def Exceptions(self, obj):
        ''' Представление исключений '''
        res = '\n'.join(obj)
        if res:
            pass
        else:
            res = self.NONE

        res = '\n'.join((self.EXCEPTIONS, add_tab(res)))
        return res

    def Parents(self, obj):
        ''' Возвращает текст, который соответствует представлению предков'''
        res = '\n'.join(obj)
        if res:
            pass
        else:
            res = self.NONE

        res = '\n'.join((self.PARENTS, add_tab(res)))
        return res

    def BlockOperators(self, obj):
        ''' Представляет совокупность операторов, как одно целое '''
        get_column = lambda iterable: 2 if len(iterable) <= 10 else 3
        obj = list(obj)
        columns = get_column(obj)
        res = to_columns(obj, columns)

        if res:
            return res
        else:
            return self.NONE

    def GroupOperators(self, obj):
        ''' Представляет операторы вместе с именем класса-владельца'''
        owner, operators = obj
        if operators:
            pass
        else:
            operators = self.NONE
        res = '\n'.join((owner, add_tab(operators)))
        return res

    def Operators(self, obj):
        ''' Возвращает текст, который представляет операторы класса. '''
        obj = list(obj)
        operators_own = obj.pop(0)
        res = []
        res.append(self.OPERATORS)
        res.append(add_tab(self.OPERATORS_OWN))
        if operators_own:
            res.append(add_tab(operators_own, 2))
        else:
            res.append(add_tab(self.NONE, 2))
        res.append('')
        res.append(add_tab(self.OPERATORS_PARENT))
        if obj:
            loc_add_tab = lambda x: add_tab(x,2)
            res.extend(map(loc_add_tab, obj))
        else:
            res.append(add_tab(self.NONE, 2))
        res = '\n'.join(res)
        return res

    def Class(self, obj):
        ''' Представление класса '''
        name, doc, parents, init, operators, attrs = obj
        res = '\n'.join(obj[1:])
        res = '\n'.join((name, add_tab(res)))
        return res

    def Module(self, obj):
        ''' Представление модуля '''
        name, doc, attrs = obj
        res = '\n\n'.join(obj[1:])
        res = '\n'.join((name, add_tab(res)))
        return res


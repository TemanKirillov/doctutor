#!/usr/bin/python3 
''' Модуль представления объектов в строковом виде.'''

class I:
    from itertools import zip_longest
    from math import ceil

def add_tab(text, number=1, as_space=None):
    ''' Добавляет в text для каждой строки символы \t в количестве заданном number.    '''

    if as_space is None:
        pasted = '\t'
    else:
        pasted = ' ' * as_space

    text = str(text)

    def replace(text):
        return text.replace('\n', '\n' + pasted * number)
    

    if text.endswith('\n'):
        return pasted * number + replace(text[:-1]) + '\n'
    else:
        return pasted * number + replace(text)

def to_pieces(iterable, n): 
    ''' Разбивает iterable на n списков'''
    li = list(iterable)
    if not li:
        return [list() for i in range(n)]
    else:
        in_piece = I.ceil(len(li) / n)        
        return [li[:in_piece]] + to_pieces(li[in_piece:], n-1)
        
def to_columns(iterable, n) -> 'str':
    ''' Возвращает строку из элементов iterable в n столбцов.'''
    elems = to_pieces(iterable, n)
    widths = [] #ширины для каждого столбца
    for piece in elems:
        piece = [str(i) for i in piece]
        if piece:
            width = len(max(piece, key=len))
        else:
            width = 0
        widths.append(width)    
    
    strings = I.zip_longest(*elems, fillvalue='') #строки в виде последовательности элементов
    
    text = ''
    for string in strings:
        parts_of_string = ['{:<{}}'.format(elem, width) for elem, width in zip(string, widths)]
        res = '  '.join(parts_of_string)
        if text:
            text += '\n' + res
        else:
            text = res
            
    return text

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
    
    def Default(self, obj):
        ''' Описание по умолчанию'''
        name, value, desc = obj
        desc = desc if desc else self.DESC_DEFAULT
        if len(value) >= 200:
            value = value[:200] + '...'
        
        example = '>>> {}\n{}\n'.format(name, value)
            

        res = '\n'.join( 
                (name,
                add_tab(desc),
                '',
                add_tab(example) ))

        return res

    def Param(self, obj):
        ''' Описание параметра'''
        name, kind, default, desc = obj
        name_def = name + '=' + default if default else name
        desc = desc if desc else self.DESC_DEFAULT
        res = '\n'.join( 
                (name_def, 
                add_tab(kind),
                add_tab(desc) ))
        return res

    def Params(self, obj) -> 'str instance':
        ''' Возвращает текст описания параметров '''
        res = '\n'.join(obj)
        if res:
            pass
        else:
            res = self.NONE

        res = '\n'.join((self.PARAMS, add_tab(res)))
        return res

    def Return(self, obj):
        ''' Описание возвращаемого значения'''
        desc, = obj
        res = '\n'.join((self.RETURN, add_tab(desc)))
        return res

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

    def Func(self, obj):
        ''' Возвращает отформатированный текст функции'''
        
        (name, sign, doc, params,
        return_, example, exceptions,) = obj 

        name_sign = name + sign
        res = [doc]
        res.extend([params, return_, example, exceptions])
        res = '\n\n'.join(res)
        res = '\n'.join((name_sign, add_tab(res)))
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

    def Attrs(self, obj):
        ''' Представление последовательности атрибутов '''
        res = '\n\n'.join(obj)
        return res

    def GroupAttrs(self, obj):
        ''' Представление группы атрибутов '''
        name, attrs = obj
        if not attrs:
            attrs = self.NONE
        res = '\n'.join((name, add_tab(attrs)))
        return res

    def class_cls(self, class_):
        res = '\n'.join(class_[1:])
        res = class_.name + add_tab(res)
        return res

    def module(self, module_):
        res = '\n'.join(module_[1:])
        res = module_.name + add_tab(res)
        return res


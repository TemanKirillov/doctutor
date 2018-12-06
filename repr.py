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
    OPERATORS = 'Операторы и протоколы'
    OPERATORS_OWN = 'Собственная реализация'
    OPERATORS_PARENT = 'Наследована от'
    ATTRS = 'Атрибуты'

    
    def Default(self, obj):
        ''' Описание по умолчанию'''
        res = '\n'.join((repr(obj), add_tab(self.DESC_DEFAULT)))
        return res

    def Param(self, obj):
        ''' Описание параметра'''
        name, kind, default, desc = obj._.name, obj._.kind, obj._.default, obj._.desc
        name_def = name + '=' + default if default else name
        desc = desc if desc else self.DESC_DEFAULT
        res = '\n'.join( 
                (name_def, 
                add_tab(kind),
                add_tab(desc) ))
        return res

    def Params(self, obj) -> 'str instance':
        ''' Возвращает текст описания параметров '''
        res = '\n'.join(iter(obj))
        if res:
            pass
        else:
            res = self.NONE

        res = '\n'.join((self.PARAMS, add_tab(res)))
        return res

    def Return(self, obj):
        ''' Описание возвращаемого значения'''
        desc = obj._.desc
        if desc:
            pass
        else:
            desc = self.NO_INFO
        res = '\n'.join((self.RETURN, add_tab(desc)))
        return res

    def Func(self, obj):
        ''' Возвращает отформатированный текст функции'''
        
        (name, sign, doc, params,
        return_, example, exceptions,) = (
        obj._.name, obj._.sign, obj._.doc, obj._.params, 
        obj._.return_, obj._.example, obj._.exceptions,)

        name_sign = name + sign
        res = [doc]
        res.extend([params, return_, example, exceptions])
        res = '\n\n'.join(res)
        res = '\n'.join((name_sign, add_tab(res)))
        return res

    def Named(self, obj):
        ''' Представление именованного объекта '''
        name, content = obj._.name, obj._.content
        if not content:
            content = self.NONE
        res = '\n'.join((name, add_tab(content)))
        return res

    def Attrs(self, obj):
        ''' Представление последовательности атрибутов '''
        res = '\n\n'.join(obj)
        return res

    def AttrsAll(self, obj):
        ''' Представление всех атрибутов объекта. Состоит из групп атрибутов '''
        res = '\n\n'.join(obj)
        if not res:
            res = self.NONE
        return '\n'.join([self.ATTRS, add_tab(res)])

    def Block(self, obj):
        ''' Представление блока '''
        name, desc, content = obj._.name, obj._.desc, obj._.content
        if not desc:
            desc = self.DESC_DEFAULT
        if not content:
            content = self.NONE
        res = '\n\n'.join((desc, content))
        res = '\n'.join((name, add_tab(res)))
        return res

    def GroupAttrs(self, obj):
        ''' Представление группы атрибутов '''
        name, attrs = obj
        if not attrs:
            attrs = self.NONE
        res = '\n'.join((name, add_tab(attrs)))
        return res


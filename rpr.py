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
    IMPORTED = 'Импорт'
    INTERNAL = 'Внутренний'
    OWN = 'Собственная реализация'

    def repr_by_obj(self, obj):
        ''' Возвращает представление контента переданного объекта obj'''
        tp = obj['type']
        content = obj['content']
        method = getattr(self, tp)
        return method(content)

    def Param(self, content):
        ''' Описание параметра'''
        name =    content['name']
        kind =    content['kind']
        default = content['default']
        desc =    content['desc']
        name_def = name + '=' + default if default else name
        desc = desc if desc else self.DESC_DEFAULT
        res = '\n'.join( 
                (name_def, 
                add_tab(kind),
                add_tab(desc) ))
        return res

    def Params(self, content):
        ''' Возвращает текст описания параметров '''
        objs = list(content.values())
        res = '\n'.join(map(self.repr_by_obj, objs))
        if res:
            pass
        else:
            res = self.NONE

        res = '\n'.join((self.PARAMS, add_tab(res)))
        return res

    def Return(self, content):
        ''' Описание возвращаемого значения'''
        desc = content
        if desc:
            pass
        else:
            desc = self.NO_INFO
        res = '\n'.join((self.RETURN, add_tab(desc)))
        return res


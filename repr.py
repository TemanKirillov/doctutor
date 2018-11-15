#!/usr/bin/python3 
''' Модуль представления объектов в строковом виде.'''


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


    def exceptions(self, iterable: 'of Except'):
        ''' Возвращает отформатированный текст исключения'''
        res = ''
        for exception in iterable:
            res += self.exception(exception)
            res += '\n'

        if res:
            pass
        else:
            res = self.NONE

        res = self.EXCEPTIONS + add_tab(res)

        return res

    def func(self, func_):
        ''' Возвращает отформатированный текст функции'''
        
        name = func_.name
        sign = func_.sign
        doc = func_.doc
        params = func_.params
        return_ = func_.return_
        example = func_.example
        exceptions = func_.exceptions

        name_sign = name + (sign if sign else '')
        res = doc if doc else ''
        res += '\n'.join([params, return_, example, exceptions])
        res = name_sign + add_tab(res)
        return res

    def parents(self, iterable):
        ''' Возвращает текст, который соответствует представлению предков из iterable'''

        res = self.PARENTS + '\n' + add_tab('\n'.join(iterable))

        return res

    def operators(self, own=None, *parents):
        ''' Возвращает текст, который представляет операторы класса. 
            own: экземпляр класса Operators с собственными операторами класса
            parents: экземпляры класса Operators с операторами родительских классов'''

        get_column = lambda iterable: 2 if len(iterable) <= 10 else 3

        res = ''        
        res += self.OPERATORS + '\n'
        res += add_tab(self.OPERATORS_OWN + '\n') 
        if own is None or not own.operators:
            res += add_tab(self.NONE, 2)
        else:
            columns = get_column(own.operators)
            res += add_tab(to_columns(own.operators, columns), 2)

        for parent in parents:
            if parent.operators:
                res += add_tab(self.OPERATORS_PARENT + ' ' + parent.self + '\n') 
                columns = get_column(parent.operators)
                res += add_tab(to_columns(parent.operators, columns), 2)
            else:
                res += add_tab(self.NONE, 2)
        
        res += '\n\n'

        return res

    def attrs(self, *groups):
        res = ''
        for group in groups:
            res += group.name + '\n'
            res += add_tab('\n'.join(group.attrs))
            res += '\n'

        return res



    def class_cls(self, class_):
        res = '\n'.join(class_[1:])
        res = class_.name + add_tab(res)
        return res

    def module(self, module_):
        res = '\n'.join(module_[1:])
        res = module_.name + add_tab(res)
        return res


""" 
Идеалогия: 
    1) Сущности для представления (если это не строки типа doc) описываются классами семейства namedtuple. 
    2) Представлением сущности в виде строки для пользователя занимается класс Repr и его производные.
    3) Нюансы реализации Repr скрыты и могут переопределяться в дочерних классах.
Класс Repr и его подклассы"""
import inspect
import builtins
import re
import operator
import json

def in_builtins(obj):
    ''' является ли объект атрибутом модуля __builtins__'''
    objs_builtins = list(builtins.__dict__.values())
    return obj in objs_builtins

def make_func(func):
    ''' Конструктор экземпляра Func из объекта реальной функции.'''

    gen_partial = False #метод сгенерирован functools.partialmethod


    name = func.__name__
    try:
        s = inspect.signature(func)
    except ValueError: #функция builtin не содержит метода __text_signature__ и не может вернуть сигнатуру
        s = None
    except IndexError: #когда метод сгенерирован функцией partialmethod
        s = None
        gen_partial = True

    if s is None:
        sign = None
        return_ = None
    else:
        sign = str(s) 
        return_ = s.return_annotation

    doc = inspect.getdoc(func)

    try:
        params = make_params(func)
    except ValueError:
        params = None

    example = None
    exceptions = None

def make_params(obj):
    res = list()
    sign = inspect.signature(obj)
    for name, param in sign.parameters.items():
        res.append(Param(name, param.kind, param.default, param.annotation))
    return res

def get_example(obj, name_parent=None, name_obj=None):    
    
    if name_obj is None:
        name_obj = obj.__name__
    res = ''
    try:
        module = obj.__module__ #для некоторых методов, типа __init__
    except AttributeError:
        module = None
        
    if in_builtins(obj) or module == '__main__' or name_parent is None: 
        name = name_obj
    
    else:    
        name = '{}.{}'.format(name_parent, name_obj)
    
    res += '>>> ' + name + '\n'
    res += repr(obj)
    return res
    
def get_view_func(func, name_parent=None, example=None, name_func=None):
    
    if name_func is None:
        name_func = func.__name__
        
    gen_partial = False #метод сгенерирован functools.partialmethod
    
    sign = None
    try:
        sign = str(inspect.signature(func))
    except ValueError: #Если builtin get_view_func
        pass
    except IndexError: #когда метод сгенерирован функцией partialmethod
        gen_partial = True
        
    params = get_params(func)
    
    res = name_func + (sign if sign else '') + '\n' + \
          '\t' + '<Описание>' + '\n' + \
          (add_tab(func.__text_signature__+'\n') if hasattr(func, '__text_signature__') and func.__text_signature__ else '') 
    res += '\tМетод сгенерирован функцией functools.partialmethod\n' if gen_partial else ''
    res += add_tab(inspect.getdoc(func)) + '\n' + \
          '\n' + \
          '\t' + 'Параметры' + '\n' + \
          add_tab(params if params else 'Отсутствуют\n', 2) + \
          '\n' + \
          '\t' + 'Возвращаемое значение' + '\n' + \
          '\t\t' + '<Описание>' + '\n' + \
          '\n' + \
          '\t' + 'Пример' + '\n' + \
          add_tab(example if example else get_example(func, name_parent, name_obj=name_func), 2) + '\n' + \
          '\n' + \
          '\t' + 'Исключения' + '\n' + \
          '\t\t' + '<Описание исключения>' + '\n' + \
          '\t\t\t' + '<Пример>' + '\n\n'
          
    return res

def is_imp(name, module):
    ''' True для импортированных классов, функций и модулей'''
    obj = getattr(module, name)
    module_obj = inspect.getmodule(obj)#модуль, где отпределён объект
    if module_obj is module:
        return False
    else:
        if inspect.isroutine(obj) or inspect.isclass(obj) or inspect.ismodule(obj):  #функции, дескрипторы; классы; модули
            return True
        else: #иные объекты считать константами
            return False    
    
def get_view_attrs(names, parent, as_const=False):
    ''' Выдаёт представление для имён, если они атрибуты объекта'''
    res = ''
    for name in names:                
        obj = getattr(parent, name)
        if inspect.isclass(obj) and not as_const:
            res += get_view_class(obj)
        elif inspect.isroutine(obj) and not as_const: #функции, дескрипторы
            res += get_view_func(obj, name_parent=parent.__name__, name_func=name)
        else:
            res += const(name, repr(obj), name_parent=parent.__name__)
    return res        
    
    
def get_view_module(module):   
    res = ( module.__name__ + '\n' +
            '<Описание>' + '\n' + 
            str(inspect.getdoc(module)) + '\n' + 
            '\n' )

    if hasattr(module, '__all__'): #явно определён основной инстументарий
        instr_main = sorted(module.__all__)
        instr_imp = []
        instr_incl = []
    else:
        all_ = dir(module)
        instr_imp = sorted(i for i in all_ if is_imp(i, module)) #импортированные иструменты
        instr_incl = sorted(set(i for i in all_ if i.startswith('_')) - set(instr_imp)) #инструменты для внутреннего пользования (импорт не рассматриваем)
        
        instr_main = sorted(set(all_) - set(instr_incl) - set(instr_imp)) #основные инструменты
                
    res += 'Основные инструменты\n' if instr_main else ''
    res += add_tab(get_view_attrs(instr_main, module))
    res += '\n'
        
    res += 'Импортированные инструменты\n' if instr_imp else ''
    res += add_tab(get_view_attrs(instr_imp, module, as_const=True))
    res += '\n'
    
    res += 'Внутренние инструменты\n' if instr_incl else ''
    res += add_tab(get_view_attrs(instr_incl, module))
    res += '\n'    
        
    return res

def method_to_operator(name_method, name_class):
    
    iden = re.match('_*\w{,1}', name_class).group().casefold()
    dict_ = {'__abs__': 'abs(%s)' % iden,
             '__add__': '%s + other' % iden,
             '__and__': '%s & other' % iden,
             '__bool__': 'bool(%s)' % iden,
             '__bytes__': 'bytes(%s)' % iden,
             '__call__': '%s()' % iden,
             '__ceil__': 'math.ceil(%s)' % iden,
             '__complex__': 'complex(%s)' % iden,
             '__contains__': '<item> in %s' % iden,
             '__copy__': 'copy.copy(%s)' % iden,
             '__deepcopy__': 'copy.deepcopy(%s)' % iden,
             '__delattr__': 'del %s.<attr>' % iden,
             '__delitem__': 'del %s[<item>]' % iden,
             '__dir__': 'dir(%s)' % iden,
             '__divmod__': 'divmod(%s, other)' % iden,
             '__enter__': 'support with',
             '__eq__': '%s == other' % iden,
             '__exit__': 'support with',
             '__float__': 'float(%s)' % iden,
             '__floor__': 'math.floor(%s)' % iden,
             '__floordiv__': '%s // other' % iden,
             '__format__': 'format(%s, <format>)' % iden,
             '__ge__': '%s >= other' % iden,
             '__getattribute__': '%s.<attr>' % iden,
             '__getitem__': '%s[<item>]' % iden,
             '__getnewargs__': 'support serialize',
             '__getstate__': 'support serialize',
             '__gt__': '%s > other' % iden,
             '__hash__': 'hash(%s)' % iden,
             '__hex__': 'hex(%s)' % iden,
             '__iadd__': '%s += other' % iden,
             '__iand__': '%s &= other' % iden,
             '__imul__': '%s *= other' % iden, 
             '__index__': 'other[%s]' % iden,
             '__instancecheck__': 'isinstance(other, %s)' % name_class,
             '__int__': 'int(%s)' % iden,
             '__ilshift__': '%s <<= other' % iden,
             '__imod__': '%s %%= other' % iden,
             '__invert__': '~%s' % iden,             
             '__ior__': '%s |= other' % iden,
             '__ipow__': '%s **= other' % iden,
             '__irshift__': '%s >>= other' % iden,
             '__subclasscheck__': 'issubclass(other, %s)' % name_class,
             '__isub__': '%s -= other' % iden,
             '__ixor__': '%s ^= other' % iden,
             '__iter__': 'iter(%s)' % iden,
             '__le__': '%s <= other' % iden,
             '__len__': 'len(%s)' % iden,
             '__lshift__': '%s << other' % iden,
             '__lt__': '%s < other' % iden,
             '__missing__': '%s.__missing__(<key>)' % iden,
             '__mod__': '%s %% other' % iden,
             '__mul__': '%s * other' % iden,
             '__ne__': '%s != other' % iden,
             '__neg__': '-%s' % iden,
             '__next__': 'next(%s)' % iden,
             '__oct__': 'oct(%s)' % iden,
             '__or__': '%s | other' % iden,
             '__pos__': '+%s' % iden,
             '__pow__': '%s ** other' % iden,
             '__radd__': 'other + %s' % iden,
             '__rand__': 'other & %s' % iden,
             '__rdivmod__': 'divmod(other, %s)' % iden,
             '__repr__': 'repr(%s)' % iden,
             '__reversed__': 'reversed(%s)' % iden,
             '__rfloordiv__': 'other // %s' % iden,
             '__rlshift__': 'other << %s' % iden,
             '__rmod__': 'other %% %s' % iden,
             '__rmul__': 'other * %s' % iden,
             '__ror__': 'other | %s' % iden,
             '__round__': 'round(%s, n)' % iden,
             '__rpow__': 'other ** %s' % iden,
             '__rrshift__': 'other >> %s' % iden,
             '__rshift__': '%s >> other' % iden,
             '__rsub__': 'other - %s' % iden,
             '__rtruediv__': 'other / %s' % iden,
             '__rxor__': 'other ^ %s' % iden,             
             '__setattr__': '%s.<attr> = value' % iden,
             '__setitem__': '%s[<item>] = value' % iden,
             '__setstate__': 'support serialize',
             '__sizeof__': 'sys.getsizeof(%s)' % iden,
             '__str__': 'str(%s)' % iden,
             '__sub__': '%s - other' % iden,
             '__truediv__': '%s / other' % iden,
             '__trunc__': 'math.trunc(%s)' % iden,
             '__xor__': '%s ^ other' % iden
             }
    
    return dict_.get(name_method, name_method)

def methods_to_operators(names, name_class):
    list_ = []
    for name in sorted(names):
        elem = method_to_operator(name, name_class)
        list_.append(elem)
        
    return list_
    
def get_operators(cls):
    methods_all = (i for i in dir(cls) if i.startswith('__')) #все __-методы, которые реализованы и которые наследуются 
    black_list = [ #методы и данные, которые определены в классе, но в списке они не выводятся
                          '__del__',
                          '__dict__',
                          '__doc__',
                          '__class__',
                          '__init__',
                          '__init_subclass__', 
                          '__module__',
                          '__new__',
                          '__subclasshook__',
                          '__reduce__',
                          '__reduce_ex__',
                          '__weakref__']
    
    #словарь (объект класса, спискок имён )
    attrs = DictValueList()    
    for attr in inspect.classify_class_attrs(cls):
        name = attr.name
        if name.startswith('__') and name not in black_list: #расценивать __ как реализацию оператора или протокола
            attrs[attr.defining_class] = name
    res = ''        
    res += 'Поддержка операторов и протоколов\n'
    res += '\tСобственная реализация\n'
    
    get_column = lambda opers: 2 if len(opers) <= 10 else 3
    parents = [item for item in cls.__mro__[1:]]
    
    if attrs.get(cls, False):
        opers = methods_to_operators(attrs[cls], cls.__name__)
        res += add_tab(to_columns(opers, get_column(opers)), 2)
    else:
        res += add_tab('Отсутствует', 2)
    #res += '\n'
    
    for parent in parents:
        if attrs.get(parent, False):
            res += '\n\n\tНаследована от ' + parent.__name__ + '\n'
            opers = methods_to_operators(attrs[parent], cls.__name__)
            res += add_tab(to_columns(opers, get_column(opers)), 2)
    
    res += '\n\n'
    
    return res

    

    
def get_init(cls, example=None):
    sign = None
    try:
        sign = str(inspect.signature(cls))
    except ValueError: #Если built-in class
        pass
    
    params = get_params(cls)
    
    res = cls.__name__ + (sign if sign else '()') + '\n' + \
          '\tИнициализация экземпляра\n\n' + \
          '\tПараметры' + '\n' + \
          add_tab(params if params else 'Отсутствуют', 2) + '\n' + \
          '\n' + \
          '\tПример' + '\n' + \
          add_tab(example if example else get_example(cls), 2) + '\n' + \
          '\n' + \
          '\t' + 'Исключения' + '\n' + \
          '\t\t' + '<Описание исключения>' + '\n' + \
          '\t\t\t' + '<Пример>' + '\n\n'
          
    return res

def get_params(obj):
    ''' Возвращает текст описания параметров функции или конструктора класса'''
    sign = None
    try:
        sign = str()
        sign = inspect.signature(obj)
        text_sign = str(sign)
        params = sign.parameters #mappingproxy(OrderedDict...
    except ValueError: #Если built-in get_view_func or class
        pass
    except IndexError: #когда метод сгенерирован функцией partialmethod
        pass
        
    #text = 'Параметры\n'
    text = ''
    if sign:
        for param in params.values():
            text += str(param) + '\n'
            text += add_tab('Вид: ' + str(param.kind) + '\n')
            
    else:
        text += '<Параметр built-in>\n'
        text += add_tab('<Описание>\n')
        
    return text

def get_view_class(cls):
    parents = '\n'.join((item.__name__ for item in cls.__mro__[1:]))
        
    res = cls.__name__ + '\n' + \
          '\t' + '<Описание>' + '\n' + \
          add_tab(inspect.getdoc(cls)) + '\n' + \
          '\n' + \
          '\t' + 'Предки' + '\n' + \
          add_tab(parents, 2) + '\n' + \
          '\n' + \
          add_tab(get_init(cls)) + '\n' + \
          '\n' + \
          add_tab(get_operators(cls))
    
    def sub(l1, l2):
        return [i for i in l1 if i not in l2]
    
    attrs = inspect.classify_class_attrs(cls)
    ag_name = operator.attrgetter('name')
    temp = [attr for attr in attrs if attr.name.startswith('__')] #расценивать __ как реализацию оператора или протокола
    attrs = sub(attrs,temp) #атрибуты без dunder-методов
    attrs_par = [attr for attr in attrs if attr.defining_class is not cls] #унаследованные атрибуты
    attrs = sub(attrs, attrs_par) #без dunder-методов и унаследованных
    attrs_incl = [attr for attr in attrs if attr.name.startswith('_')] 
    attrs = sub(attrs, attrs_incl) #без dunder-методов, унаследованных и внутренних
    attrs_main = attrs[:]
    
    list_names_par = [attr.name + ' от ' + repr(attr.defining_class) for attr in sorted(attrs_par, key=ag_name)]
    
    if list_names_par:
        res += '\tНаследованные атрибуты\n'
        res += add_tab('\n'.join(list_names_par), 2) + '\n\n'
    
    if attrs_main:    
        res += '\tОсновные атрибуты\n'
        res += add_tab(get_view_attrs(sorted(map(ag_name, attrs_main)), cls), 2) + '\n\n'
        
    if attrs_incl:
        res += '\tВнутренние атрибуты\n'
        res += add_tab(get_view_attrs(sorted(map(ag_name, attrs_incl)), cls), 2) + '\n\n'        
             
    return res

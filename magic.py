#!/usr/bin/python3 
''' Модуль для работы с "магическими" методами. '''

def convert(name_method, name_class):
    ''' Конвертирует строку с именем метода в строку с оператором. '''    
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

def convert_all(names, name_class):
    return [convert(name, name_class) for name in names]
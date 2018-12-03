#!/usr/bin/python3 

class I:
    from collections import UserDict
    from collections import namedtuple
    from collections import OrderedDict
    import copy

def namedtuple_methods(cls):
    """ Декоратор класса, который генерируется collections.namedtuple. Добавляет новые методы."""

    @classmethod
    def from_dict(cls, dct):
        return cls._make(dct[f] for f in cls._fields)

    @classmethod
    def from_json(cls, string):
        dct = json.loads(string)
        return cls.from_dict(dct)

    cls.from_dict = from_dict
    cls.from_json = from_json

    return cls

class DictValueList(I.UserDict):
    def __setitem__(self, key, value):
        if key in self:
            self[key].append(value)
        else:
            super().__setitem__(key, [value])

class InternalAttrs:
    def __get__(self, instance, owner):
        self._o_ = {}
        self._o_['getattribute'] = super(owner, instance).__getattribute__
        return self
    def __getattribute__(self, key):
        if key == '_o_':
            return super().__getattribute__(key)
        else:
            return self._o_['getattribute'](key)

class DictAttr(I.OrderedDict):
    ''' Ключи словаря также являются его атрибутами'''
    blacklist = ['__class__', '__call__', '__dict__'] #особые атрибуты, которые нельзя установить в экземпляре
    _o_ = InternalAttrs() #

    def __set(self, key, value):
        super().__setitem__(key, value)
        if key not in self._o_.blacklist:
            super().__setattr__(key, value)
    def __del(self, key):
        super().__delitem__(key)
        if key not in self._o_.blacklist:
            super().__delattr__(key)
    def __setitem__(self, key, value):
        self._o_.__set(key, value)
    def __setattr__(self, key, value):
        self._o_.__set(key, value)
    def __delitem__(self, key):
        self._o_.__del(key)
    def __delattr__(self, key):
        self._o_.__del(key)
    def __getattribute__(self, key):
        if key in self._o_.blacklist and self._o_.__contains__(key):
            return self._o_.__getitems__[key]
        else:
            return super().__getattribute__(key)

    def __deepcopy__(self, memo):
        cls = self._o_.__class__
        obj = cls()
        for key, value in self._o_.items():
            try:
                cop = I.copy.copy(value)
            except TypeError: #не копируется
                obj[key] = value
            else:
                obj[key] = cop
        return obj
        

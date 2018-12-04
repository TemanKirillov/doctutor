#!/usr/bin/python3 

class I:
    from collections import UserDict
    from collections import namedtuple
    from collections import OrderedDict

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

class GetAttrDict:
    ''' Реализует механизм доступа к ключам словаря, как к атрибутам '''
    _ = None

    def __init__(self, dct):
        self._ = dct
        
    def __getattribute__(self, key):
        if key == '_':
            return super().__getattribute__(key)
        return self._[key]

    def __setattr__(self, key, value):
        if key == '_':
            return super().__setattr__(key, value)
        self._[key] = value
        
    def __delattr__(self, key):
        if key == '_':
            return super().__delattr__(key)
        del self._[key]
        

class DictAttr(I.OrderedDict):
    ''' Ключи словаря также являются его атрибутами'''

    def __set(self, key, value):
        super().__setitem__(key, value)
        super().__setattr__(key, value)
    def __del(self, key):
        super().__delitem__(key)
        super().__delattr__(key)
    def __setitem__(self, key, value):
        self.__set(key, value)
    def __setattr__(self, key, value):
        self.__set(key, value)
    def __delitem__(self, key):
        self.__del(key)
    def __delattr__(self, key):
        self.__del(key)

class I:
    import obj
    import json
    import pprint
    import repr

def object_hook(obj):
    dct = dict(obj)
    cls = dict
    if '_type' in dct:
        _type = dct['_type']
        if _type in I.obj.__dict__:
            cls = I.obj.__dict__[_type]
    return cls(obj)

obj = I.obj.Params()
obj.a = I.obj.Param.from_iterable(['param1', 'POSITION', '3', 'Param1 for test'])
obj.b = I.obj.Param.from_iterable(['param2', 'POSITION', '"string"', 'Param2 for test'])

with open('test_json.txt', mode='w') as file:
    I.json.dump(obj, file, indent=4, separators=(',\n', ': '))

with open('test_json.txt') as file:
    obj2 = I.json.load(file, object_hook=object_hook)

print(obj2)

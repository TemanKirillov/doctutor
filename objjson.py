class I:
    import obj
    import json
    import pprint

obj = I.obj.Obj()
obj.a = 'test a'
obj.b = 'test b'

with open('test_json.txt', mode='w') as file:
    I.json.dump(obj, file, indent=4, separators=(',\n', ': '))

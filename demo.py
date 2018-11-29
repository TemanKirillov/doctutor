class I:
    import obj
    import make
    import repr
    import disp

#целевая функция
def func(a, b = 1, c: 'param C' = 10) -> 'str':
    pass

#создание объекта-посредника
obj = I.make.Make().Params(func)

# представление без коррекции 
string = I.disp.recursive(obj)
print(string)

#коррекция и добавление новой информации
obj.a.desc = '<description of param "a">'
for param in obj:
    if param.kind == 'POSITIONAL_OR_KEYWORD':
        param.kind = 'Стандартный'

#Представление коррекции 

string = I.disp.recursive(obj)
print(string)



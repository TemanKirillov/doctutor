class I:
    import obj
    import make
    import repr
    import disp
    import string

#целевая функция
func = I.string.capwords

#создание объекта-посредника
obj = I.make.Make().Func(func)

# представление без коррекции 
string = I.disp.recursive(obj)
print(string)

#коррекция и добавление новой информации
obj.name = 'string.' + obj.name
obj.sign += ' -> string'
obj.return_.desc = 'Экземпляр класса str'
for param in obj.params:
    if param.kind == 'POSITIONAL_OR_KEYWORD':
        param.kind = 'Стандартный'


#Представление коррекции 

string = I.disp.recursive(obj)
print(string)



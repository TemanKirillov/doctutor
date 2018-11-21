class I:
    import tree
    import string

all_dunder = I.tree.getmembers('string.Template', I.string.Template, I.tree.isdunder)
print("==============all_dunder++++++++++++++")
[print(i[0]) for i in list(all_dunder)]
def pred_own_dunder(*args):
    return I.tree.isdunder(*args) and not I.tree.isinparent(*args)
own_dunder = I.tree.getmembers('string.Template', I.string.Template, pred_own_dunder) 
print("==============own_dunder++++++++++++++")
[print(i[0]) for i in list(own_dunder)]
def pred_imp_dunder(*args):
    return I.tree.isdunder(*args) and I.tree.isimp(*args)
imp_dunder = I.tree.getmembers('string.Template', I.string.Template, pred_imp_dunder) 
print("==============impdunder++++++++++++++")
[print(i[0]) for i in list(imp_dunder)]


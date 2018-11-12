import mydoc
import os
import sys
import imp

# module = imp.importlib.import_module(name_module)

__, folder, name_module, *other = sys.argv
module = imp.importlib.import_module(name_module)

string = mydoc.get_view_module(module)
path = os.path.join(folder, 'doc_{}_auto.txt'.format(name_module))
with open(path, mode='x', encoding='utf-8') as file:
    file.write(string)

os.popen(r'explorer ' + folder)
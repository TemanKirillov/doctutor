#!/usr/bin/python3 

class I:
    from collections import namedtuple
    from dispatcher import Dispatcher
    import inspect

class Component(I.namedtuple('_Component', 'name obj'):
    pass

class Leaf(Component):
    pass

class Container(Component):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.leaves = []
        self.containers = []

    def add(self, component):
        if isinstance(component, Leaf):
            self.leaves.append()

converter = Dispatcher()
converter.key = lambda c: c.obj

@converter.bind(I.inspect.ismodule):
def _(component):
    name = component.name
    obj = component.obj
    doc = component.leaves.pop('__doc__', None)
    attrs = []
    for leaf in self.leaves:
        attrs.append(Default(leaf.name, leaf.obj, None))
    for container in containers:
        attrs.append(converter(container))
    res = Module(name, doc, attrs)
    return res



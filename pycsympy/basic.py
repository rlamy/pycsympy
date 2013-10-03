class Basic(object):
    def as_term(self):
        return Add(0, {self: 1})

    def __add__(self, other):
        return add(self, other)
    __radd__ = __add__


class Symbol(Basic):
    def __init__(self, name):
        self.name = name

from pycsympy.add import Add, add

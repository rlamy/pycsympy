class Basic(object):
    def as_term(self):
        return Add(0, {self: 1})

    def __add__(self, other):
        return add(self, other)
    __radd__ = __add__

    def __pow__(self, other):
        return power(self, other)

    def __rpow__(self, other):
        return power(other, self)


class Symbol(Basic):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name
    __repr__ = __str__

from pycsympy.add import Add, add, power

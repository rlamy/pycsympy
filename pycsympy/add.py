from pycsympy.basic import Basic

class Add(Basic):
    def __init__(self, term, _dict):
        self.numberterm = term
        self._dict = _dict

    def as_term(self):
        return self

    def __eq__(self, other):
        if not isinstance(other, Add):
            return False
        return self.numberterm == other.numberterm and self._dict == other._dict

    def __iadd__(self, other):
        if isinstance(other, int):
            other = Add(other, {})
        elif not isinstance(other, Add):
            other = other.as_term()
        self.numberterm += other.numberterm
        for key, value in other._dict.iteritems():
            self._dict.setdefault(key, 0)
            self._dict[key] += value
        return self

    def canonicalize(self):
        if not self._dict:
            return self.numberterm
        if self.numberterm == 0 and len(self._dict) == 1:
            value, = self._dict
            if self._dict[value] == 1:
                return value
        return self


def add(*args):
    if not args:
        return 0
    it = iter(args)
    result = next(it).as_term()
    for arg in it:
        result += arg
    return result.canonicalize()

class Monomial(Basic):
    def __init__(self, dct):
        self._dict = dct

def power(base, expt):
    if expt == 0:
        return 1
    elif expt == 1:
        return base
    return Monomial({base: expt})

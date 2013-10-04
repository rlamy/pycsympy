from pycsympy.basic import Basic
from pycsympy.multinomial import multinomial_coefficients

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

    def __str__(self):
        parts = [str(self.numberterm)]
        parts += ['%s*%s' % (c, x) for x, c in self._dict.iteritems()]
        return ' + '.join(parts)
    __repr__ = __str__

    def canonicalize(self):
        if not self._dict:
            return self.numberterm
        if self.numberterm == 0 and len(self._dict) == 1:
            value, = self._dict
            if self._dict[value] == 1:
                return value
        return self

    def terms(self):
        parts = [self.numberterm] if self.numberterm else []
        return parts + list(self._dict)


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

    def __eq__(self, other):
        if not isinstance(other, Monomial):
            return False
        return self._dict == other._dict

    def __str__(self):
        return ' * '.join(['%s**%s' % (b, e) for b, e in self._dict.iteritems()])

    def expand(self):
        if len(self._dict) == 1:
            (base, expt), = self._dict.iteritems()
            terms = base.terms()
            expansion_dict = multinomial_coefficients(len(terms), expt)
            return expr_from_dict(expansion_dict, terms)
        else:
            return self



def expr_from_dict(rep, gens):
    """Convert a multinomial form into an expression. """
    dct = {}
    for monom, coeff in rep.iteritems():
        term = {}
        for x, n in zip(gens, monom):
            if n > 0:
                term[x] = n
        dct[Monomial(term)] = coeff
    return Add(0, dct)

def power(base, expt):
    if expt == 0:
        return 1
    elif expt == 1:
        return base
    return Monomial({base: expt})

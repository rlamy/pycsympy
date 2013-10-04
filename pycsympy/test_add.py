from pycsympy.basic import Symbol
from pycsympy.add import Add, Monomial

def test_add_basic():
    x, y, z = map(Symbol, 'xyz')
    assert isinstance(x + y, Add)
    assert isinstance(x + 0, Symbol)
    assert (x + y) + z == x + (y + z)
    assert x + y == y + x

def test_pow():
    x, y, z = map(Symbol, 'xyz')
    assert x**0 == 1
    assert isinstance(z**1, Symbol)
    assert isinstance((x + y)**2, Monomial)

def test_expand():
    x, y, z = map(Symbol, 'xyz')
    print ((x+y+z)**4).expand()
    assert ((x+y)**2).expand() == Add(0, {x**2: 1, Monomial({x: 1, y: 1}): 2,
                                          y**2: 1})

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

from pycsympy.basic import Symbol
from pycsympy.add import Add

def test_add_basic():
    x, y, z = map(Symbol, 'xyz')
    assert isinstance(x + y, Add)
    assert isinstance(x + 0, Symbol)
    assert (x + y) + z == x + (y + z)
    assert x + y == y + x

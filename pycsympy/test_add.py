from pycsympy.basic import Symbol
from pycsympy.add import Add, add

def test_add_basic():
    x, y, z = map(Symbol, 'xyz')
    assert isinstance(add(x, y), Add)
    assert isinstance(add(x, 0), Symbol)
    assert add(add(x, y), z) == add(x, add(y, z))
    assert add(x, y) == add(y, x)

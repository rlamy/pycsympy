#!/usr/bin/env python

from timeit import default_timer as clock
from random import randint
from pycsympy.basic import Symbol
from pycsympy.multinomial import multinomial_coefficients

x = Symbol("x")
y = Symbol("y")
z = Symbol("z")
w = Symbol("w")


def bench_expand1():
    "e=(x+y+z+w)**60; e.expand()"
    e = (x+y+z+w)**60
    return e.expand()

def _expand1():
    """multinomial_coefficients(4, 60)"""
    return multinomial_coefficients(4, 60)

def bench_expand2():
    "e=(x+y+z+1)**50; e.expand()"
    e = (x+y+z+1)**50
    e = e.expand()

def expand3():
    """(x**y + y**z + z**x)**100"""
    e = (x**y + y**z + z**x)**100
    return e.expand()

def add1():
    "Add(x,<random integer>,y), 2000x"
    for i in range(2000):
        x + randint(0, 1000000) + y

def sum1():
    s = 0
    for i in range(401):
        s += x**i


benchmarks = [
        bench_expand1,
        _expand1,
        bench_expand2,
        expand3,
        add1,
        sum1,
        ]

report = []
for b in benchmarks:
    for _ in range(10):
        t = clock()
        b()
        t = clock()-t
        print "%65s: %f" % (b.__doc__, t)
    print

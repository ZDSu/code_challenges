from fibonnaci_sequence import *


def test_fibonnaci():
    assert fib_rec(10) == 55
    assert fib_dyn(10) == 55
    assert fib_iter(23) == 28657
    assert fib_iter(1) == 1


def test_fibonnaci_more_tests():
    assert fib_rec(0) == 0
    assert fib_dyn(2) == 1
    assert fib_iter(3) == 2
    assert fib_rec(4) == 3
    assert fib_rec(5) == 5
    assert fib_dyn(6) == 8
    assert fib_iter(7) == 13
    assert fib_rec(8) == 21
    assert fib_dyn(9) == 34
    assert fib_iter(11) == 89
    assert fib_rec(12) == 144
    assert fib_dyn(13) == 233
    assert fib_iter(14) == 377
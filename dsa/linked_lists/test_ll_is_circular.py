from ll_is_circular import *


def test_is_circular():
    # CREATE CYCLE LIST
    a = Node(1)
    b = Node(2)
    c = Node(3)

    a.nextnode = b
    b.nextnode = c
    c.nextnode = a # Cycle Here!

    # CREATE NON CYCLE LIST
    x = Node(1)
    y = Node(2)
    z = Node(3)

    x.nextnode = y
    y.nextnode = z

    assert cycle_check(a) is True
    assert cycle_check(x) is False
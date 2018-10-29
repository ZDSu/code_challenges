from ll_reversal import *


def test_reversal():
    # Create a list of 4 nodes
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)

    # Set up order a,b,c,d with values 1,2,3,4
    a.nextnode = b
    b.nextnode = c
    c.nextnode = d

    assert a.nextnode.value == 2
    assert b.nextnode.value == 3
    assert c.nextnode.value == 4
    assert d.nextnode is None

    reverse(a)

    assert d.nextnode.value == 3
    assert c.nextnode.value == 2
    assert b.nextnode.value == 1
    assert a.nextnode is None
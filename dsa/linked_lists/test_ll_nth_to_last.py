from ll_nth_to_last import *


def test_nth_to_last():
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)
    e = Node(5)

    a.nextnode = b
    b.nextnode = c
    c.nextnode = d
    d.nextnode = e

    target_node = nth_to_last_node(2, a)
    assert target_node.value == 4
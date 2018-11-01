class Node:

    def __init__(self, value):
        self.value = value
        self.nextnode  = None


def nth_to_last_node(n, head):
    right = left = head
    for _ in range(n - 1):
        if not right.nextnode:
            raise LookupError('n is larger than list')
        right = right.nextnode
    while right.nextnode:
        right = right.nextnode
        left = left.nextnode
    return left


def nth_to_last_node(n, head):
    right = left = head
    for _ in range(n):
        if not right.nextnode:
            raise LookupError('n is larger than list')
        right = right.nextnode
    while right:
        right = right.nextnode
        left = left.nextnode
    return left
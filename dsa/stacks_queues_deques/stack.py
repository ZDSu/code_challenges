class Node:
    def __init__(self, val=None):
        self.val = val
        self._next = None

    def __repr__(self):
        return f'Node value is {self.val}'

    def __str__(self):
        return f'Node value is {self.val}'


class Stack():
    def __init__(self):
        self.top = None
        self._length = 0

    def repr(self):
        return f'Top of stack is {self.top.val}'

    def len(self):
        return self._length

    def push(self, val):
        node = Node(val)
        if self.top:
            node._next = self.top
        self.top = node
        self._length += 1
        return self.top.val

    def pop(self):
        node = self.top
        self.top = self.top._next
        self._length -= 1
        return node.val

    def peek(self):
        return self.top.val
"""Node class for binary search tree."""


class Node:
    """Tree node."""

    def __init__(self, key, value, left=None, right=None, parent=None):
        self.key = key
        self.payload = value
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

"""Node class for binary search tree."""


class Node:
    """Tree node."""

    def __init__(self, key, value, left=None, right=None, parent=None):
        """Constructor."""
        self.key = key
        self.payload = value
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        """Returns True if node has a left child, else False."""
        return self.leftChild

    def hasRightChild(right):
        """Returns True if node has a right child, else False."""
        return self.rightChild

    def isLeftChild(self):
        """Returns True if node is a left child, else False."""
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        """Returns True if node is a right child, else False."""
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        """Returns True if node is a root, else False."""
        return not self.parent

    def isLeaf(self):
        """Returns True if node is a leaf, else False."""
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        """Returns True if node has any children, else False."""
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        """Returns True if node has both left and right children, else False."""
        return self.rightChild and self.leftChild

    def replaceNodeData(self, key, value, left, right):
        """Replace node data."""
        self.key = key
        self.payload = value
        self.leftChild = left
        self.rightChild = right
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self

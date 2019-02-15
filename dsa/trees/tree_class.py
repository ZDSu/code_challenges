"""Class definition of a tree."""


class BinaryTree:
    """Class definition of a binary tree."""

    def __init__(self, rootObj):
        """Initialization."""
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, node):
        """Insert new node as left child."""
        if not self.leftChild:
            self.leftChild = BinaryTree(node)
        else:
            root = BinaryTree(node)
            root.leftChild = self.leftChild
            self.leftChild = root

    def insertRight(self, node):
        """Insert new node as right child."""
        if not self.rightChild:
            self.rightChild = BinaryTree(node)
        else:
            root = BinaryTree(node)
            root.rightChild = self.rightChild
            self.rightChild = root

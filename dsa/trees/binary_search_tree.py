"""Binary search tree class."""


from tree_node import Node


class BinarySearchTree:
    """Binary search tree class."""

    def __init__(self):
        """Constructor."""
        self.root = None
        self.size = 0

    def __setitem__(self, key, value):
        """Implement assignment to be able to use bracket notation (i.e., self[key])."""
        self.insert(key, value)

    def __getitem__(self, key):
        """Allows use of bracket notation to retrieve tree node value (i.e., self[key])."""
        self.get(key)

    def __len__(self):
        """Allows use of the len() built-in method."""
        return self.size

    def __iter__(self):
        """Iterate through the binary search tree, called on root."""
        return self.root.__iter__()

    def length(self):
        """Return size of tree."""
        return self.size

    def insert(self, key, value):
        """Insert a new node into tree."""
        if self.root:
            self._insert(key, value, self.root)
        else:
            self.root = Node(key, value)
        self.size += 1

    def _insert(self, key, value, currentNode):
        """Insert helper method."""
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._insert(key, value, currentNode.leftChild)
            else:
                currentNode.leftChild = Node(key, value, parent=currentNode)
        else:
            if currentNode.hasRightChild():
                self._insert(key, value, currentNode.rightChild)
            else:
                currentNode.rightChild = Node(key, value, parent=currentNode)

    def get(self, key):
        """Retrieve the value for a given key."""
        if self.root:
            if self._get(key, self.root):
                print('get', self._get(key, self.root).payload)
                return self._get(key, self.root).payload

    def _get(self, key, currentNode):
        """Get helper method."""
        if not currentNode:
            return
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self._get(key, currentNode.leftChild)
        else:  # key > currentNode.key
            return self._get(key, currentNode.rightChild) 

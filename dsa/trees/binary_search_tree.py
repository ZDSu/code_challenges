"""Binary search tree class."""


from tree_node import Node


class BinarySearchTree:
    """Binary search tree class."""

    def __init__(self):
        """Constructor."""
        self.root = None
        self.size = 0

    def __setitem__(self, key, value):
        """Implement assignment to be able to use bracket notation (i.e., self[key] = value)."""
        self.insert(key, value)

    def __getitem__(self, key):
        """Allows use of bracket notation to retrieve tree node value (i.e., self[key])."""
        self.get(key)

    def __delitem__(self, key):
        """Allows use of bracket notation to delete node (i.e., del self[key])."""
        self.delete(key)

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

    def delete(self, key):
        """Delete the node with the given key."""
        if self.size == 1 and self.root.key == key:
            self.root = None
            self.size -= 1
        if self.size > 1:
            if self._get(key, self.root):
                self._delete(self._get(key, self.root))
                self.size -= 1
        else:
            raise KeyError('Key not in tree')

    def _delete(self, currentNode):
        """Delete helper method."""
        if currentNode.isLeaf():  # leaf node
            if currentNode == currentNode.parent.leftChild:
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.rightChild = None
        else:  # node has one child
            if currentNode.hasLeftChild():
                if currentNode.isLeftChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.leftChild
                elif currentNode.isRightChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.leftChild
                else:  # node is root
                    currentNode.replaceNodeData(currentNode.leftChild.key, \
                                        currentNode.leftChild.payload, \
                                        currentNode.leftChild.leftChild, \
                                        currentNode.leftChild.rightChild)
            else:  # has right child
                if currentNode.isLeftChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.rightChild
                elif currentNode.isRightChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.rightChild
                else:  # node is root
                    currentNode.replaceNodeData(currentNode.rightChild.key, \
                                        currentNode.rightChild.payload, \
                                        currentNode.rightChild.leftChild, \
                                        currentNode.rightChild.rightChild)

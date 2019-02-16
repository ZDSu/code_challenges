"""Binary search tree class."""


class BinarySearchTree:
    """Binary search tree class."""

    def __init__(self):
        """Constructor."""
        self.root = None
        self.size = 0

    def length(self):
        """Return size of tree."""
        return self.size

    def __len__(self):
        """Allows use of the len() built-in method."""
        return self.size

    def __iter__(self):
        """Iterate through the binary search tree, called on root."""
        return self.root.__iter__()

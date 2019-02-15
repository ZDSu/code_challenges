"""Representation of a tree using a list of lists."""


def BinaryTree(r):
    """
    Define root of binary tree.

    r is the root at index 0 followed by its left and right children at indices 1 and 2, respectively.
    """
    return [r, [], []]


def insertLeft(root, newBranch):
    """
    Add a left child to node.

    If left child exists, add new left child by making the existing left child the left child in the newly inserted list.
    """
    t = root.pop(1)  # obtain the left child list, which is at index 1

    if len(t) > 1:  # if there is an existing left child
        root.insert(1, [newBranch, t, []])
    else:
        root.insert(1, [newBranch, [], []])

    return root


def insertRight(root, newBranch):
    """
    Add a right child to node.

    If right child exists, add new right child by making the existing right child the right child in the newly inserted list.
    """
    t = root.pop(2)  # obtain the right child list, which is at index 2

    if len(t) > 1:  # if there is an existing right child
        root.insert(2, [newBranch, [], t])
    else:
        root.insert(2, [newBranch, [], []])

    return root


def getRootVal(root):
    """Return root value."""
    return root[0]


def setRootVal(root, value):
    """Set a new root value."""
    root[0] = value


def getLeftChild(root):
    """Return left child."""
    return root[1]


def getRightChild(root):
    """Return right child."""
    return root[2]

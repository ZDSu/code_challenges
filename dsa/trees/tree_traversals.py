"""Tree traversal as functions."""

from tree_class import BinaryTree as BT


def preorder(root):
    """Preorder Traversal of Tree."""
    if not root:
        return

    print(root.getRootValue())
    if root.leftChild:
        preorder(root.getLeftChild())
    if root.rightChild:
        preorder(root.getRightChild())


def inorder(root):
    """Inorder Traversal of Tree."""
    if not root:
        return

    if root.leftChild:
        inorder(root.getLeftChild())
    print(root.getRootValue())
    if root.rightChild:
        inorder(root.getRightChild())


def postorder(root):
    """Postorder Traversal of Tree."""
    if not root:
        return

    if root.leftChild:
        postorder(root.getLeftChild())
    if root.rightChild:
        postorder(root.getRightChild())
    print(root.getRootValue())

r = BT('a')
r.insertLeft('b')
r.insertLeft('c')
r.insertRight('d')
r.insertRight('e')
print(preorder(r))
print(inorder(r))
print(postorder(r))

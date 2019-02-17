"""Test cases for bst check."""

from bst_check import *


def test_true():
    """Test that BST is True."""
    root = Node(10, "Hello")
    root.left = Node(5, "Five")
    root.right = Node(30, "Thirty")

    assert verify(root) is True


def test_false():
    """Test that BST is False."""
    root = Node(10, "Ten")
    root.right = Node(20, "Twenty")
    root.left = Node(5, "Five")
    root.left.right = Node(15, "Fifteen")

    assert verify(root) is False  # 15 is to the left of 10

# https://leetcode.com/problems/n-ary-tree-preorder-traversal/


# runtime 100 ms, 23$; memory 17.7 MB, 5%
"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        traverse = []

        def _walk(node):
            if node:
                traverse.append(node.val)
                if node.children:
                    for child in node.children:
                        _walk(child)
        _walk(root)
        return traverse

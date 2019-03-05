# https://leetcode.com/problems/n-ary-tree-level-order-traversal/


"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        traverse = []
        queue = [root]

        while queue:
            curr = queue.pop(0)
            traverse.append(curr.val)
            if curr.children:
                for child in curr.children:
                    queue.append(child)
        return traverse

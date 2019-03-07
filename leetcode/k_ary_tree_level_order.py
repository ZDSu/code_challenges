# https://leetcode.com/problems/n-ary-tree-level-order-traversal/


# runtime 124 ms, 14%; memory 17.6 MB, 5.5%
"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []

        traverse = []
        queue = [root]

        while queue:
            level = []
            for _ in range(len(queue)):
                curr = queue.pop(0)
                level.append(curr.val)
                if curr.children:
                    for child in curr.children:
                        queue.append(child)
            traverse.append(level)
        return traverse

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
            level = kids = []
            for _ in range(len(queue)):
                curr = queue.pop(0)
                level.append(curr.val)
                if curr.children:
                    kids.append(children)
            traverse.append(level)
            queue = kids
        return traverse


# runtime 108 ms, 28%; memory 17.7 MB, 5.5%
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []

        traverse = []
        queue = [root]

        while queue:
            level = []
            kids = []
            for node in queue:
                level.append(node.val)
                if node.children:
                    kids += node.children
            traverse.append(level)
            queue = kids
        return traverse


# test cases:
# null
# {"$id":"1","children":[],"val":44}

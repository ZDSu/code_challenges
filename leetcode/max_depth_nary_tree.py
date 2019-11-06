# https://leetcode.com/problems/maximum-depth-of-n-ary-tree/
# https://leetcode.com/articles/maximum-depth-of-n-ary-tree


# runtime 100 ms, 18%; memory 17.7 MB, 5%
# then ran again, runtime 88 ms, 65%; memory 17.6 MB, 5%
# then ran again, runtime 92 ms, 42%; memory 17.7 MB, 5%
"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0

        depth = 0
        queue = [root]

        while queue:
            level = []
            depth += 1
            for _ in range(len(queue)):
                curr = queue.pop(0)
                if curr.children:
                    level += curr.children
            if level:
                queue += level

        return depth

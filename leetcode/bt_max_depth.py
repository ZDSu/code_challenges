# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
# https://leetcode.com/explore/learn/card/data-structure-tree/17/solve-problems-recursively/535/


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# runtime 52 ms, 16%; memory 13.7 MB, 87%
# runtime 28 ms, 89%; memory 14.4 MB, 95%
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        queue = [root]
        depth = 0
        while queue:
            for _ in range(len(queue)):
                curr = queue.pop(0)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            depth += 1
        return depth


# test cases:
# []
# [1,2,3,4,5]  root: 1; next level: 2, 3;  next level: 4,5 are children of 2

# https://leetcode.com/problems/balanced-binary-tree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        left = 0
        right = 0

        queue = [root]

        while queue:
            level = []
            curr = queue.pop(0)
            if curr.left:
                level.append(curr.left)
                left += 1
            if curr.right:
                level.append(curr.right)
                right += 1
            queue.append(level)

        return abs(left - right) <= 1

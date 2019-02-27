# https://leetcode.com/problems/univalued-binary-tree/


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        val = root.val

        def _traverse(node):
            if node:
                if node.val != val:
                    return False
                if node.left:
                    _traverse(node.left)
                if node.right:
                    _traverse(node.right)
        _traverse(root)
        return True

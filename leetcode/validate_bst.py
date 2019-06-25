# https://leetcode.com/problems/validate-binary-search-tree/
# https://leetcode.com/articles/validate-binary-search-tree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def traverse(node, prev, child):
            if node:
                if child == 'left':
                    if node.val > prev:
                        return False
                if child == 'right':
                    if node.val < prev:
                        return False
                if node.left:
                    traverse(node.left, node.val, 'left')
                if node.right:
                    traverse(node.right, node.val, 'right')
            return True

        return traverse(root, None, None)

# test cases:
# [1,1]   returns False
# [10,5,15,null,null,6,20]   returns False
# [2,1,3]   returns True

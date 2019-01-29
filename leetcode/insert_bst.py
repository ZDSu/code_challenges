# https://leetcode.com/problems/insert-into-a-binary-search-tree/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoBST(self, root, value):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        current = root
        
        while current:
            if current.val > value:
                if current.left is not None:
                    current = current.left
                else:
                    if value > current.val:
                        current.right = TreeNode(value)
                    else:
                        current.left = TreeNode(value)
                    return root
            else:
                if current.right is not None:
                    current = current.right
                else:
                    if value > current.val:
                        current.right = TreeNode(value)
                    else:
                        current.left = TreeNode(value)
                    return root


# 120 ms, 92%
class Solution:
    def insertIntoBST(self, root, value):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        curr = root
        while curr:
            if curr.val < value:
                if curr.right:
                    curr = curr.right
                else:
                    curr.right = TreeNode(value)
                    break
            else:
                if curr.left:
                    curr = curr.left
                else:
                    curr.left = TreeNode(value)
                    break
        return root

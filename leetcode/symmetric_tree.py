# https://leetcode.com/problems/symmetric-tree/
# https://leetcode.com/articles/symmetric-tree/


# test case:
# [1,2,2,null,3,null,3]  returns false


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        queue = [root, root]
        
        while queue:
            t1 = queue.pop(0)
            t2 = queue.pop(0)
            if not t1 and not t2:
                continue
            if (not t1 or not t2) or (t1.val != t2.val):
                return False
            queue.append(t1.left)
            queue.append(t2.right)
            queue.append(t1.right)
            queue.append(t2.left)
        
        return True
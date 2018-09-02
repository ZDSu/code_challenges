# https://leetcode.com/problems/path-sum/description/
# (401-Java whiteboard final)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, target):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        
        def _walk(node, temp): 
            if node is None:
                return
            
            temp += node.val
            if temp == target and node.left is None and node.right is None:
                return True
            
            if node.left:               
                status = _walk(node.left, temp)
                if status is True:
                    return True
                
            if node.right:
                status = _walk(node.right, temp)
                if status is True:
                    return True
            
            return False
        return _walk(root, 0)


# simpler solution:
class Solution:
    def hasPathSum(self, root, target):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False

        if not root.left and not root.right:
            return root.val == target

        return self.hasPathSum(root.left, target - root.val) or self.hasPathSum(root.right, target - root.val)


# test cases:
# [], 1
# [7,0,null,-1,-6,null,1,null,null,-7], 0
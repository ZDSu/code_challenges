# https://leetcode.com/problems/same-tree/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p or not q:
            return False
        
        queue1 = [p]
        queue2 = [q]
        
        while queue1:
            if not queue2:
                return False
            curr1 = queue1.pop(0)
            curr2 = queue2.pop(0)
            if curr1.val != curr2.val:
                return False
            if curr1.left:
                queue1.append(curr1.left)
            if curr1.right:
                queue1.append(curr1.right)
            if curr2.left:
                queue2.append(curr2.left)
            if curr2.right:
                queue2.append(curr2.right)
        return True
            
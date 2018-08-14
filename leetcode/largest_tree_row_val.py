# https://leetcode.com/problems/find-largest-value-in-each-tree-row/description/
# Note: use row_max = -float("inf") for negative infinity value


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        
        largest = []        
        queue = [root]
        
        while queue:
            row_max = -float("inf")  # or could use row_max = queue[0].val
            row = []
            for node in queue:
                if node.val > row_max:
                    row_max = node.val
                if node.left:
                    row.append(node.left)
                if node.right:
                    row.append(node.right)
            largest.append(row_max)
            queue = row
        return largest


# test cases: [] , [0, -1]
# https://leetcode.com/problems/validate-binary-search-tree/
# https://leetcode.com/articles/validate-binary-search-tree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True

        def _check(curr):
            if curr.right:
                if curr.right.val <= curr.val or curr.right.val <= root.val:
                    return False
                _check(curr.right)
            if curr.left:
                if curr.left.val >= curr.val or curr.left.val <= root.val:
                    return False
                _check(curr.left)
            return True

        valid = _check(root)
        return valid

# test case: 
# [1,1]   returns False
# [10,5,15,null,null,6,20]   returns False
# [2,1,3]   returns True

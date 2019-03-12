# https://leetcode.com/problems/kth-smallest-element-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        if not root:
            return

        def _walk(node):
            nonlocal k
            if node:
                # if node.left:
                _walk(node.left)
                if k == 1:
                    return node.val
                k -= 1
                # if node.right:
                _walk(node.right)

        return _walk(root)

# https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/928/
# https://leetcode.com/problems/binary-tree-preorder-traversal/


# runtime 20 ms, 100%; memory 10.9 MB, 12%
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if not root:
            return res

        def travel(node):
            if not node:
                return
            res.append(node.val)
            if node.left:
                travel(node.left)
            if node.right:
                travel(node.right)

        travel(root)
        return res

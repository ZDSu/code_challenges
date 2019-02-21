# https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/929/
# https://leetcode.com/problems/binary-tree-inorder-traversal/


# (recursive) runtime 20 ms, 100%; memory 10.7 MB, 62%
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
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
            travel(node.left)
            res.append(node.val)
            travel(node.right)

        travel(root)
        return res

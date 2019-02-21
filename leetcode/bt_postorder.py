# https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/930/
# https://leetcode.com/problems/binary-tree-postorder-traversal/


# (recursive) runtime 20ms, 100%; memory 10.9 MB, 14%
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
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
            travel(node.right)
            res.append(node.val)

        travel(root)
        return res

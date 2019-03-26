# https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/930/
# https://leetcode.com/problems/binary-tree-postorder-traversal/


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# (recursive) runtime 20ms, 100%; memory 10.9 MB, 14%
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


# runtime 36 ms, 74%; memory 13.3 MB, 6%
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        res = []
        def _traverse(node):
            if node:
                if node.left:
                    _traverse(node.left)
                if node.right:
                    _traverse(node.right)
                res.append(node.val)
        _traverse(root)
        return res

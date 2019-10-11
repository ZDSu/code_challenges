# https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/928/
# https://leetcode.com/problems/binary-tree-preorder-traversal/
# https://leetcode.com/articles/binary-tree-preorder-transversal  (Premium)


# (recursive) runtime 20 ms, 100%; memory 10.9 MB, 12%
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


# (recursive) runtime 20 ms, 100%; memory 10.8 MB, 52%
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
            travel(node.left)
            travel(node.right)

        travel(root)
        return res


# (iterative) runtime 32ms, 14%; memory 10.7 MB, 84%
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
        stack = [root]

        if not root:
            return res

        while stack:
            curr = stack.pop()
            res.append(curr.val)
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)

        return res

# https://leetcode.com/problems/univalued-binary-tree/
# https://leetcode.com/articles/univalued-binary-tree/


# runtime: 16 ms, 100%; memory 10.8 MB, 75%
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        val = root.val
        queue = [root]

        while queue:
            curr = queue.pop(0)
            if curr.val != val:
                return False
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        return True


# (recursive) runtime: 16 ms, 100%; memory 10.9 MB, 16%
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def univalued(root, last_val):
            if not root:
                return True
            if root.val != last_val:
                return False
            return univalued(root.left, root.val) and univalued(root.right, root.val)

        return univalued(root, root.val)

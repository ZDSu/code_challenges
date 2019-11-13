# https://leetcode.com/problems/search-in-a-binary-search-tree/description/
# Note: just need to return the node when the value is found and the subtree of that node is done automatically. I thought I had to make a list with the node and it's subtree nodes after so was over complicating it!
# https://leetcode.com/articles/search-in-a-bst/ (Premium)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root, value):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return []

        current = root

        while current:
            if current.val == value:
                return current
            elif current.val < value:
                current = current.right
            else:
                current = current.left
        return []


# slightly better solution (less code but not more performant)
class Solution:
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        while root and root.val != val:
            if val < root.val:
                root = root.left
            else:
                root = root.right
        return root


class Solution:
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root or not val:
            return

        queue = [root]

        while queue:
            curr = queue.pop(0)
            if curr.val == val:
                return curr
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        return


# test cases:
# [4,2,7,1,3], 5   returns []
# [18,2,22,null,null,null,63,null,84,null,null], 63   returns [63,null,84]


#  according to solutions, this is fastest, but runs slower than my other solutions
class Solution:
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        while root:
            if root.val == val:
                return root
            elif root.val > val:
                root = root.left
            elif root.val < val:
                root = root.right
        return None


# and then this one gets 100% but is basically the same as the solution above
class Solution:
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        while root:
            if root.val == val:
                return root
            if root.val < val:
                root = root.right
            else:
                root = root.left
        return


# runtime 60 ms, 99%; memory 15.9 MB, 23%
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        while root:
            if root.val == val:
                return root
            elif root.val < val:
                root = root.right
            else:
                root = root.left

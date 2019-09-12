# https://leetcode.com/problems/symmetric-tree/
# https://leetcode.com/articles/symmetric-tree/


# Both solutions are same time [O(n)], 40 ms, 99%
# space complexity: recursive is O(h) [h = height of tree], iterative is O(n) [n = nodes]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# iterative
# runtime 24 ms, 73%; memory 12.1 MB, 29%
class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        queue = [root, root]

        while queue:
            t1 = queue.pop(0)
            t2 = queue.pop(0)
            if not t1 and not t2:
                continue
            if (not t1 or not t2) or (t1.val != t2.val):
                return False
            queue.append(t1.left)
            queue.append(t2.right)
            queue.append(t1.right)
            queue.append(t2.left)

        return True


# recursive
class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def isMirror(t1, t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            return (t1.val == t2.val) and isMirror(t1.right, t2.left) and isMirror(t1.left, t2.right)

        return isMirror(root, root)


# runtime 16 ms, 97%; memory 11.9 MB, 82%
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        def compare(node1, node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            return node1.val == node2.val and \
                compare(node1.left, node2.right) and \
                compare(node2.left, node1.right)

        return compare(root, root)


# Pathrise solution
# runtime 16 ms, 93%; memory 12 MB, 64%
class Solution(object):
    def areEqual(self, node1, node2):
        if not node1 and not node2:
            return True
        if not node1 or not node2:
            return False

        left = self.areEqual(node1.left, node2.right)
        right = self.areEqual(node1.right, node2.left)

        return left is True and right is True and node1.val == node2.val


    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        if not root.left and not root.right:
            return True
        return self.areEqual(root.left, root.right)


# Pathrise solution with early exit
# runtime 20 ms, 77%; memory 12.2 MB, 7%
class Solution(object):
    def areEqual(self, node1, node2):
        if not node1 and not node2: return True
        if not node1 or not node2: return False
        if node1.val != node2.val:
            return False

        left = self.areEqual(node1.left, node2.right)
        right = self.areEqual(node1.right, node2.left)

        return left and right


    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        if not root.left and not root.right:
            return True
        return self.areEqual(root.left, root.right)


# test case: [1]  returns True

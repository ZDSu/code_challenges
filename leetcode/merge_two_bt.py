# https://leetcode.com/problems/merge-two-binary-trees/description/
# https://leetcode.com/articles/merge-two-binary-trees/


# runtime 68 ms, 68%
# runtime 88 ms, 74%; memory 13.4 MB, 30%
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1 or not t2:
            return t1 or t2

        queue = [(t1, t2)]

        while queue:
            one, two = queue.pop(0)
            if one and two:
                one.val += two.val
            if one.left and two.left:
                queue.append((one.left, two.left))
            elif two.left:
                one.left = two.left
            if one.right and two.right:
                queue.append((one.right, two.right))
            elif two.right:
                one.right = two.right
        return t1


# runtime 88 ms, 74%; memory 13.8 MB;9%
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1 or not t2:
            return t1 or t2

        t1.val += t2.val

        t1.left = self.mergeTrees(t1.left, t2.left)

        t1.right = self.mergeTrees(t1.right, t2.right)

        return t1


# above solution with print statements for debugging
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1 or not t2:
            return t1 or t2
        print('start')
        print('0', t1.val, t2.val)
        t1.val += t2.val

        if t1.left: print('l1', t1.left.val)
        if t2.left: print('l2', t2.left.val)
        print('left')
        t1.left = self.mergeTrees(t1.left, t2.left)
        if t1.left: print('lafter', t1.left.val)

        if t1.right: print('r1', t1.right.val)
        if t2.right: print('r2', t2.right.val)
        print('right')
        t1.right = self.mergeTrees(t1.right, t2.right)
        if t1.right: print('rafter', t1.right.val)

        return t1

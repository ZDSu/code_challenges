# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# runtime 40 ms, 68%; memory 13.3 MB, 5%
class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if not root:
            return res

        queue = [root]
        forward = True

        while queue:
            level = []
            for _ in range(len(queue)):
                curr = queue.pop(0)
                level.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            if not forward:
                level.reverse()
            res.append(level)
            forward = not forward

        return res


# leetcode says this way is faster, but all give same results
# runtime 40 ms, 68%; memory 13.3 MB, 5%
class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if not root:
            return res
        
        queue = [root]
        
        while queue:
            level = []
            for _ in range(len(queue)):
                curr = queue.pop(0)
                level.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            if len(res) % 2 == 1:
                level = level[::-1]
            res.append(level)
        
        return res


# runtime 40 ms, 68%; memory 13.4 MB, 5%
class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        res = []
        queue = [root]
        left = True

        while queue:
            level = []
            for _ in range(len(queue)):
                curr = queue.pop(0)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                if left:
                    level.append(curr.val)
                else:
                    level.insert(0, curr.val)
            res.append(level)
            left = not left
        return res

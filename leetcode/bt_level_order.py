# https://leetcode.com/problems/binary-tree-level-order-traversal/
# https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/931/
# https://leetcode.com/articles/binary-tree-level-order-traversal


# runtime 28 ms, 82%; memory 11.5 MB, 46%
# done again and now runtime 44 ms, 52%; memory 13.2 MB, 12.5%
# and 13.3 MB memory when line 35 in code below is after line 30
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        res = []
        queue = [root]

        while queue:
            level = []
            for _ in range(len(queue)):
                curr = queue.pop(0)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                level.append(curr.val)
            res.append(level)

        return res


# test cases:
# []  returns []
# [1,2,3,4,5] returns [[1],[2,3],[4,5]]


# Approach 2 solution code
from collections import deque
class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        levels = []
        if not root:
            return levels

        level = 0
        queue = deque([root,])
        while queue:
            # start the current level
            levels.append([])
            # number of elements in the current level
            level_length = len(queue)

            for i in range(level_length):
                node = queue.popleft()
                # fulfill the current level
                levels[level].append(node.val)

                # add child nodes of the current level
                # in the queue for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # go to next level
            level += 1

        return levels

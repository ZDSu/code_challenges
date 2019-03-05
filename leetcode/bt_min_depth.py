# https://leetcode.com/problems/minimum-depth-of-binary-tree/submissions/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        depth = 0
        queue = [root]

        while queue:
            for _ in range(len(queue)):
                curr = queue.pop(0)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            depth += 1
        return depth

# test cases:
# [0]  returns 1
# [1,2]  returns 2

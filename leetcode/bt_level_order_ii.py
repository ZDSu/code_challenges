# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# runtime: 60 ms, 16%; memory: 13.5 MB, 5%
# runtime: 16 ms, 98%; memory: 12.2 MB, 80%
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        traverse = []

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
            traverse.insert(0, level)
        return traverse

# https://leetcode.com/problems/average-of-levels-in-binary-tree/
# https://leetcode.com/problems/average-of-levels-in-binary-tree/solution/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# runtime 60 ms, 75%; memory 15.6MB, 16%
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:
            return []

        res = []        
        queue = [root]
        while queue:
            level_sum = 0
            nodes = len(queue)
            for _ in range(nodes):
                curr = queue.pop(0)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                level_sum += curr.val
            res.append(level_sum / nodes)
        return res

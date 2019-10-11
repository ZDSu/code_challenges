# https://leetcode.com/problems/minimum-depth-of-binary-tree/
# https://leetcode.com/articles/minimum-depth-of-binary-tree  (Premium)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# runtime: 32 ms, 87%; memory 14.4 MB, 90%
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        depth = 0
        minimum = float('inf')
        queue = [root]
        while queue:
            for _ in range(len(queue)):
                curr = queue.pop(0)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                if not curr.left and not curr.right:
                    if depth + 1 < minimum:
                        minimum = depth + 1
            depth += 1
        return minimum


# after Pathrise lesson
# runtime 32 ms, 73%; memory 14.6 MB, 67%
def getHeight(root):
    if not root:
        return 0

    if not root.left:
        right = getHeight(root.right)
        return right + 1
    if not root.right:
        left = getHeight(root.left)
        return left + 1

    left = getHeight(root.left)
    right = getHeight(root.right)
    return min(left, right) + 1

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        left = getHeight(root.left)
        right = getHeight(root.right)

        if not left or not right:
            return (left or right) + 1

        return min(left, right) + 1

# test cases:
# [0]  returns 1
# [1,2]  returns 2
# [1,null,2]  returns 2
# [-9,-3,2,null,4,4,0,-6,null,-5]  returns 3

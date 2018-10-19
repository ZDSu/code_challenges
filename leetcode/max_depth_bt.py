# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/


class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        queue = [root]
        level = 0
        
        while queue:
            curr = queue.pop(0)
            if not queue:
                level += 1
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        return level


# test cases:
# []
# [1,2,3,4,5]  root: 1; next level: 2, 3;  next level: 4,5 are children of 2

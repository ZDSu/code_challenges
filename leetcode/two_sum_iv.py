# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/
# https://leetcode.com/articles/two-sum-iv


# runtime 72 ms, 79%; memory 16.1 MB, 95%
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        def traverse(node, seen):
            if node:
                if k - node.val in seen:
                    return True
                else:
                    seen.add(node.val)
                if traverse(node.left, seen) or traverse(node.right, seen):
                    return True
        return traverse(root, set())

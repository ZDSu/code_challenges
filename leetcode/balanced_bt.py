# https://leetcode.com/problems/balanced-binary-tree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True

        left = 1
        right = 1

        if root.left:
            queue1 = [root.left]

            while queue1:
                level1 = []
                left += 1

                curr = queue1.pop(0)
                if curr.left or curr.right:

                    if curr.left:
                        level1.append(curr.left)
                    if curr.right:
                        level1.append(curr.right)
                if level1:
                    queue1 += level1

        if root.right:
            queue2 = [root.right]
            while queue2:
                level2 = []
                right += 1

                curr = queue2.pop(0)
                if curr.left or curr.right:

                    if curr.left:
                        level2.append(curr.left)
                    if curr.right:
                        level2.append(curr.right)
                if level2:
                    queue2 += level2

        return abs(left - right) <= 1


# my test cases (if tree visualizer is true):
# [3,9,5,20,null,3,null,15,3,null,4,2,3,7]  says false but output true and should be true
# [3,9,5,20,null,null,15,3,null,4,2,3,7]  says false, but outputs true and should be true


# test cases:
# []  returns true
# [1]  returns true
# [1,null,2,null,3] returns false
# [1,2,2,3,null,null,3,4,null,null,4]  returns false

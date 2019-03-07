# https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        res = []
        coords = []
        ht = {}

        root.val = (0, 0, root.val)
        queue = [root]

        while queue:
            level = []
            for node in queue:
                curr = queue.pop(0)
                x = curr.val[0]
                y = curr.val[1]
                if x in ht:
                    ht[x].append(curr.val)
                else:
                    ht[x] = [curr.val]
                level.append(curr)
                if curr.left:
                    curr.left.val = (x-1, y-1, curr.left.val)
                    queue.append(curr.left)
                if curr.right:
                    curr.right.val = (x+1, y-1, curr.right.val)
                    queue.append(curr.right)
            coords.append(level)
        for key in sorted(ht.keys()):
            temp = []
            for node in ht[key]:
                temp.append(node[2])
            res.append(temp)
        return res






# test cases:
# [0,2,1,3,null,null,null,4,5,null,7,6,null,10,8,11,9]  returns [[4,10,11],[3,6,7],[2,5,8,9],[0],[1]]
# getting [[4,10,11],[3,7,6],[2,5,8,9],[0],[1]]

print(ht[key])
[(-3, -3, 4), (-3, -5, 10), (-3, -5, 11)]
[(-2, -2, 3), (-2, -4, 7), (-2, -4, 6)]
[(-1, -1, 2), (-1, -3, 5), (-1, -5, 8), (-1, -5, 9)]
[(0, 0, 0)]
[(1, -1, 1)]

print(temp)
[4, 10, 11]
[3, 7, 6]
[2, 5, 8, 9]
[0]
[1]
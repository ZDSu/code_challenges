# https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/
# this challenge is #987. #314 is similar. Difference is:
#  314: If two nodes are in the same row and column, the order should be from left to right. (also only for premium users)
# 987: If two nodes have the same position, then the value of the node that is reported first is the value that is smaller.


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
# I think the above solution would pass problem #314


# test cases:
# [0,2,1,3,null,null,null,4,5,null,7,6,null,10,8,11,9]  returns [[4,10,11],[3,6,7],[2,5,8,9],[0],[1]]
# getting [[4,10,11],[3,7,6],[2,5,8,9],[0],[1]]  (probably #314 solution)
# [0,5,1,9,null,2,null,null,null,null,3,4,8,6,null,null,null,7] returns [[9,7],[5,6],[0,2,4],[1,3],[8]]
# [0,2,1,3,null,5,22,9,4,12,25,null,null,13,14,8,6,null,null,null,null,null,27,24,26,null,17,7,null,28,null,null,null,null,null,19,null,11,10,null,null,null,23,16,15,20,18,null,null,null,null,null,21,null,null,29] returns [[13,28],[9,24,27,16],[3,8,14,11,19],[2,4,12,7,17,26,15,20,23],[0,5,6,10,21,29],[1,25,18],[22]]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        res = []
        ht = {}
        root.val = (0, 0, root.val)
        queue = [root]

        while queue:
            curr = queue.pop(0)
            x = curr.val[0]
            y = curr.val[1]
            if x in ht:
                ht[x].append(curr.val)
            else:
                ht[x] = [curr.val]
            if curr.left:
                curr.left.val = (x-1, y-1, curr.left.val)
                queue.append(curr.left)
            if curr.right:
                curr.right.val = (x+1, y-1, curr.right.val)
                queue.append(curr.right)
        for key in sorted(ht.keys()):
            temp = []
            for i in range(len(ht[key])):
                if 1 <= i <= len(ht[key]):
                    if ht[key][i][0] == ht[key][i - 1][0] and ht[key][i][1] == ht[key][i - 1][1]:
                        if ht[key][i][2] < ht[key][i - 1][2]:
                            temp.insert(-1,ht[key][i][2])
                            continue
                temp.append(ht[key][i][2])
            res.append(temp)
        return res
# doesn't pass [0,2,1,3,null,5,22,9,4,12,25,null,null,13,14,8,6,null,null,null,null,null,27,24,26,null,17,7,null,28,null,null,null,null,null,19,null,11,10,null,null,null,23,16,15,20,18,null,null,null,null,null,21,null,null,29]   ... passing 20/30 tests
# https://leetcode.com/problems/binary-tree-vertical-order-traversal/

# this challenge is #314. #987 is similar. Difference is:
#  314: If two nodes are in the same row and column, the order should be from left to right. Also has test case [] (also only for premium users)
# 987: If two nodes have the same position, then the value of the node that is reported first is the value that is smaller.

"""
Binary Tree Vertical Order Traversal (Medium) (Premium)
Given a binary tree, return the vertical order traversal of its nodes' values.  (ie, from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.

Examples 1:
Input: [3,9,20,null,null,15,7]
      3
     / \
    9  20
      /  \
     15  7
Output:
[
    [9],
    [3,15],
    [20],
    [7]
]

Examples 2:
Input: [3,9,8,4,0,1,7]
       3
    /    \
   9      8
  / \    / \
 4   0  1   7
Output:
[
  [4],
  [9],
  [3,0,1],
  [8],
  [7]
]

Examples 3:
Input: [3,9,8,4,0,1,7,null,null,null,2,5] (0's right child is 2 and 1's left child is 5)

       3
    /     \
   /       \
   9        8
  /\       /\
 /  \     /  \
4   0     1   7
     \   /
      2  5
Output:
[
  [4],
  [9,5],
  [3,0,1],
  [8,2],
  [7]
]
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        pass



# test cases:
# []  returns []
# [-64,12,18,-4,-53,null,76,null,-51,null,null,-93,3,null,-31,47,null,3,53,-81,33,4,null,-51,-44,-60,11,null,null,null,null,78,null,-35,-64,26,-81,-31,27,60,74,null,null,8,-38,47,12,-24,null,-59,-49,-11,-51,67,null,null,null,null,null,null,null,-67,null,-37,-19,10,-55,72,null,null,null,-70,17,-4,null,null,null,null,null,null,null,3,80,44,-88,-91,null,48,-90,-30,null,null,90,-34,37,null,null,73,-38,-31,-85,-31,-96,null,null,-18,67,34,72,null,-17,-77,null,56,-65,-88,-53,null,null,null,-33,86,null,81,-42,null,null,98,-40,70,-26,24,null,null,null,null,92,72,-27,null,null,null,null,null,null,-67,null,null,null,null,null,null,null,-54,-66,-36,null,-72,null,null,43,null,null,null,-92,-1,-98,null,null,null,null,null,null,null,39,-84,null,null,null,null,null,null,null,null,null,null,null,null,null,-93,null,null,null,98]
# returns [[-4,78,73,-77,-54,-36],[12,-51,-81,4,8,3,-30,-33,86,81,98,24],[-64,-53,-31,47,-35,-67,-37,72,-4,-38,-31,-31,-18,-66,-72,43],[18,-93,33,-51,-38,47,-24,-11,80,44,-91,-42,-40,70,-93],[76,3,-64,26,-31,-19,10,-85,-96,67,34,-92,-1],[3,-44,-60,12,-59,-51,67,-88,48,-26,92,72],[53,-81,27,60,-55,-70,72,56,-88,-98,-84],[11,-49,-90,90,-34,-27,-67,98],[74,17,-17,-65,-53,39],[37]]



# not my solution
# runtime: 52 ms, 7%; memory 14.1 MB, 14%
from collections import defaultdict, deque
from queue import Queue
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        nodes = defaultdict(list)
        q = Queue()
        q.put((root, 0))
        result = []
        while q.qsize() > 0:
            node, level = q.get()
            nodes[level].append(node.val)
            if node.left:
                q.put((node.left, level-1))
            if node.right:
                q.put((node.right, level + 1))

        for key in sorted(nodes.keys()):
            result.append(nodes[key])
        return result

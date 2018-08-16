# https://www.hackerrank.com/challenges/tree-level-order-traversal/problem
# see site for tree setup

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def levelOrder(root):
    #Write your code here
    traverse = ''
    queue = [root]
    while queue:
        current = queue.pop(0)
        traverse += str(current.info) + ' '
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return print(traverse[:-1])
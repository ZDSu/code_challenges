# https://www.hackerrank.com/challenges/tree-inorder-traversal/problem


"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def inOrder(root):
    #Write your code here
    traverse = ''
    
    def _walk(node=None):
        nonlocal traverse
        if not node:
            return
        if node.left:
            _walk(node.left)
        traverse += str(node.info) + ' '
        if node.right:
            _walk(node.right)
    
    _walk(root)
    return print(traverse[:-1])

# or just:
def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.info, end=" ")
        inOrder(root.right)
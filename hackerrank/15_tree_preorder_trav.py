# https://www.hackerrank.com/challenges/tree-preorder-traversal/problem


"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def preOrder(root):
    #Write your code here
    traverse = ''
    
    def _walk(node=None):
        nonlocal traverse
        if node is None:
            return
        
        traverse += str(node.info) + ' '
        
        if node.left:
            _walk(node.left)
        
        if node.right:
            _walk(node.right)

    _walk(root)
    
    return print(traverse[:-1])


# simpler
def preOrder(root):
    #Write your code here
    if root:
        print(root.info, end = ' ')
        preOrder(root.left)
        preOrder(root.right)
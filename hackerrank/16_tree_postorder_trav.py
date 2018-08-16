# https://www.hackerrank.com/challenges/tree-postorder-traversal/problem


"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def postOrder(root):
    #Write your code here
    traverse = ''
    
    def _walk(node=None):
        nonlocal traverse
        if node is None:
            return
        
        if node.left:
            _walk(node.left)
            
        if node.right:
            _walk(node.right)
            
        traverse += str(node.info) + ' '
    
    _walk(root)
    
    return print(traverse[:-1])

# simpler
def postOrder(root):
    #Write your code here
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(root.info, end=' ')
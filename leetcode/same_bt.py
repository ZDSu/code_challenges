# https://leetcode.com/problems/same-tree/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if (p and not q) or (q and not p):
            return False
        if not p and not q:
            return True
        
        queue1 = [p]
        queue2 = [q]
        
        while queue1:
            curr1 = queue1.pop(0)
            curr2 = queue2.pop(0)
            if curr1.val != curr2.val:
                return False
            if curr1.left and curr2.left:
                queue1.append(curr1.left)
                queue2.append(curr2.left)
            elif (curr1.left and not curr2.left) or (curr2.left and not curr1.left):
                return False
            if curr1.right and curr2.right:
                queue1.append(curr1.right)
                queue2.append(curr2.right)
            elif (curr1.right and not curr2.right) or (curr2.right and not curr1.right):
                return False                
        return True


# test cases: 
# [] [] 
# [1,2] [1, null, 2]

# How to think about this for a 1-line solution:
# The example submission for the 100% C solution is about 30 lines. Yikes. Think more, code less. Only one line is needed.
# If tree p is empty, then return true if and only if q is empty. Otherwise p is not empty, so return true if and only if q is also not empty, its root value matches the root value of q, and both left and right subtrees match.
# Now both of these alternatives return, so we can put both branches in a ternary expression and return its value instead:

# bool isSameTree(struct TreeNode* p, struct TreeNode* q) {
#   return !p ? !q : q && p->val == q->val && isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
# }


# another shorter python solution:
def isSameTree(self, p, q):
    stack = []
    stack.append((p,q))
    while stack:
        p, q = stack.pop()
        if not p and not q:
            continue

	if p and q:   
	    if p.val != q.val:
		return False
	    else:
	        stack.append((p.left, q.left))
	        stack.append((p.right, q.right))
	else:
	    return False

    return True
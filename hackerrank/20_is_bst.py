# https://www.hackerrank.com/challenges/is-binary-search-tree/problem
# only passing 5 test cases


""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""
def check_binary_search_tree_(root):
    if root:
        queue = [root]
        while queue:
            current = queue.pop(0)
            if current.left:
                if current.left.data > current.data:
                    return 'No'
                queue.append(current.left)
            if current.right:
                if current.right.data < current.data:
                    return 'No'
                queue.append(current.right)
        return 'Yes'
    return 'No'
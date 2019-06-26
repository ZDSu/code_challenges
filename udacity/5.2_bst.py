class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        if not self.root:
            self.root = Node(new_val)
            return

        curr = self.root
        while curr:
            if curr.value < new_val:
                if not curr.right:
                    curr.right = Node(new_val)
                    return
                curr = curr.right
            else:
                if not curr.left:
                    curr.left = Node(new_val)
                    return
                curr = curr.left

    def search(self, find_val):
        curr = self.root
        while curr:
            if curr.value == find_val:
                return True
            if curr.value < find_val:
                curr = curr.right
            else:
                curr = curr.left
        return False

# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print tree.search(4)
# Should be False
print tree.search(6)

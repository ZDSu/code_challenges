# https://www.hackerrank.com/challenges/binary-search-tree-insertion/problem


#Node is defined as
#self.left (the left child of the node)
#self.right (the right child of the node)
#self.info (the value of the node)

    def insert(self, val):
        #Enter you code here.
        if not self.root:
            self.root = Node(val)
            return
        current = self.root
        while current:
            if val < current.info:
                if current.left:
                    current = current.left
                else:
                    current.left = Node(val)
                    return
            else:
                if current.right:
                    current = current.right
                else:
                    current.right = Node(val)
                    return
        return self.root
            
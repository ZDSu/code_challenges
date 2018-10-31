class Node():
    def __init__(self, value=None):
        self.val = value
        self.next = None


class SLL():
    def __init__(self):
        self.head = None
        self.tail = None

    def __repr__(self):
        return f'Head of list is ${self.head.val}'

    def __str__(self):
        return f'Head of list is ${self.head.val}'

    def insert(self, value):
        """Insert at head."""
        node = Node(value)
        if self.head:
            node.next = self.head
        self.head = node

    def append(self, value):
        """Append to tail."""
        node = Node(value)
        if not self.head:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def pop(self):
        """Remove at head."""
        if not self.head:
            raise IndexError('List is empty')
        removed_node = self.head
        self.head = self.head.next
        return removed_node.val

    def remove(self, value):
        """Remove node with given value."""
        if not self.head:
            raise IndexError('List is empty')
        
        if self.head.val = value:
            removed_node = self.head
            self.head = self.head.next
            return removed_node
            
        curr = self.head
        prev = None
        while curr:
            if curr.val == value:
                if prev:
                    prev.next = curr.next
                else:
                    self.head = curr.next
                removed_node = curr
                return curr.val
                
            prev = curr
            curr = curr.next
        raise ValueError('Value not in list')
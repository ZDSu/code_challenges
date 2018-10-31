# Note: This code has not been tested


class Node():
    def __init__(self, value=None):
        self.val = value
        self.next = None
        self.prev = None


class DLL():
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, value):
        """Insert at head of list."""
        node = Node(value)
        if not self.head:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

    def append(self, value):
        """Insert at tail of list."""
        node = Node(value)
        if not self.head:
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def pop(self):
        """Remove node at head of list."""
        if not self.head:
            raise IndexError('List is empty')
        removed_node = self.head
        self.head = removed_node.next
        self.head.prev = None
        return removed_node

    def remove(self, value):
        """Remove node with given value."""
        if not self.head:
            raise IndexError('List is empty')

        if self.head.val == value:
            return self.pop()

        curr = self.head
        prev = None
        while curr:
            if curr.val == value:
                prev.next = curr.next
                removed_node = curr
                if curr.next:
                    curr.next.prev = prev
                return removed_node
            prev = curr
            curr = curr.next
        
        raise ValueError('Value not in list')
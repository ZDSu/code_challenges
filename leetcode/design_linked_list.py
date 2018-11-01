# https://leetcode.com/problems/design-linked-list/description/


# blank ()
class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)


# Last executed input:
# ["MyLinkedList","addAtHead","addAtIndex","get","get","get"]
# [[],[1],[1,2],[1],[0],[2]]



class Node():
    def __init__(self, value):
        self.val = value
        self.next = None

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index > self.size - 1:
            return -1
        if index == 0:
            return self.head
        
        curr = self.head
        for _ in range(1, index + 1):
            curr = curr.next
        return curr.val

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        node = Node(val)
        if not self.tail:
            self.tail = node
        if self.head:
            node.next = self.head
        self.head = node
        self.size += 1

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        node = Node(val)
        if self.tail:
            self.tail.next = node
        if not self.head:
            self.head = node
        self.tail = node
        self.size += 1

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        if index > self.size:
            return
            
        if index == self.size:
            return self.addAtTail(val)
        
        if index == 0:
            return self.addAtHead(val)
        
        curr = self.head
        for idx in range(1, index - 1):
            curr = curr.next
        
        node = Node(val)
        node.next = curr.next
        curr.next = node
        if node.next is None:
            self.tail = node

        self.size += 1

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        if index > self.size:
            return
        
        if index == 0:
            self.head = self.head.next
            if not self.head:
                self.tail = None
            return
        
        curr = self.head
        for _ in range(1, index - 1):
            curr = curr.next
        if curr.next == self.tail:
            curr = self.tail
        else:
            curr.next = curr.next.next
        
        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)


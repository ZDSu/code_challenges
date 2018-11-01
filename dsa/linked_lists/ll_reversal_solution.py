class Node(object):

    def __init__(self,value):

        self.value = value
        self.nextnode = None


def reverse(head):
    curr = head
    prev = None
    while curr:
        temp = curr.nextnode
        curr.nextnode = prev
        prev = curr
        curr = temp
    head = curr
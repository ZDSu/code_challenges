# https://www.hackerrank.com/challenges/print-the-elements-of-a-linked-list/problem


# Complete the printLinkedList function below.
#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def printLinkedList(head):
    if not head:
        return
    current = head
    while current:
        print(current.data)
        current = current.next
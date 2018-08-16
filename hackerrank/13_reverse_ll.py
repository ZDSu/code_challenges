# https://www.hackerrank.com/challenges/reverse-a-linked-list/problem
# see site for SLL setup


# Complete the reverse function below.
#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def reverse(head):
    current = head
    previous = None
    while current:
        temp = current.next
        current.next = previous
        previous = current
        current = temp
    head = previous
    return head
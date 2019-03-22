# https://leetcode.com/problems/reverse-linked-list/description/
# https://leetcode.com/articles/reverse-linked-list/


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        previous = None
        
        while head:
            temp = head.next
            head.next = previous
            previous = head
            head = temp
        head = previous
        return head


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        curr = head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev


# runtime: 44 ms, 65%; memory 14.5 MB, 31%
class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        dummy = ListNode(None)
        dummy.next = head
        curr = head
        
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        dummy.next = prev
        return dummy.next


# runtime: 48 ms, 34%; memory 14.4 MB, 33%
class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        curr = head
        
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        head = prev
        return head


# runtime: 44 ms, 65%; memory 14.5 MB, 31%
class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        curr = head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

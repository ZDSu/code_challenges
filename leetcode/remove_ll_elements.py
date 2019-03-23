# https://leetcode.com/problems/remove-linked-list-elements/description/


# runtime: 80 ms, 55%; memory 16.3 MB, 19%
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return []
        dummy = ListNode(None)
        dummy.next = head
        head = dummy
        while dummy and dummy.next:
            if dummy.next.val == val:
                dummy.next = dummy.next.next
            else:
                dummy = dummy.next
        return head.next


# test cases:
# [1], 1   returns []
# [], 1   returns []
# [1], 2   returns [1]
# [1,2], 2   returns [1]
# [1,2], 1   returns [2]
# [1,1], 1   returns []
# (mine) [6,1,2,6,3,4,5,6], 6   returns [1,2,3,4,5]


# runtime: 96 ms, 22%; memory: 16.4 MB, 19%
class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return []
        
        prev = None
        curr = head
        
        while curr:
            if curr.val == val:
                if not prev:
                    head = head.next
                    curr = curr.next
                    continue
                
                prev.next = curr.next
                curr = curr.next
                continue
            
            prev = curr
            curr = curr.next
        
        return head


# runtime: 80 ms, 55%; memory 16.4 MB, 19%
class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return []

        prev = None
        curr = head

        while curr:
            if curr.val == val:
                if not prev:
                    head = curr.next
                else:
                    prev.next = curr.next
                curr = curr.next
            else:
                prev = curr
                curr = curr.next
        return head

# https://leetcode.com/problems/remove-linked-list-elements/description/


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
# [1], 1
# [], 1
# [1], 2
# [1,2], 1   returns [2]
# [1,1], 1   returns []
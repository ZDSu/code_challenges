# https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
# https://leetcode.com/articles/remove-duplicates-from-sorted-list/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return
        
        curr = head
        while curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return

        curr = head
        runner = head.next

        while curr.next and runner:
            if runner.val != curr.val:
                curr.next = runner
                curr = curr.next
            runner = runner.next
        curr.next = None
        return head


# test cases:
# [1,1,1]   returns [1]
# [1,1,2,3,3]
# []  returns None
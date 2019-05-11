# https://leetcode.com/problems/middle-of-the-linked-list/
# https://leetcode.com/articles/middle-of-the-linked-list/


# 36 ms, 81%; 13.3 MB, 5%
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow

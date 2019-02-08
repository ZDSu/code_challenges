# https://leetcode.com/problems/linked-list-cycle-ii/
# https://leetcode.com/articles/linked-list-cycle-ii/ [subscription only]


# runtime: 44 ms, 100%; memory 18.4 MB, 16.15%
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        seen = set()
        while head:
            if head in seen:
                return head
            else:
                seen.add(head)
            head = head.next

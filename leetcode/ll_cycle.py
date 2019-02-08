# https://leetcode.com/problems/linked-list-cycle/
# https://leetcode.com/articles/linked-list-cycle/


# runtime: 40 ms, 100%; memory: 16.2 MB, 92%
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        curr1 = curr2 = head
        while curr1 and curr2 and curr2.next:
            curr1 = curr1.next
            curr2 = curr2.next.next
            if curr1 is curr2:
                return True
        return False

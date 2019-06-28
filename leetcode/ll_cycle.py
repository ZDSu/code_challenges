# https://leetcode.com/problems/linked-list-cycle/
# https://leetcode.com/articles/linked-list-cycle/


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# runtime: 40 ms, 100%; memory: 16.2 MB, 92%
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        curr1 = curr2 = head
        # while curr1 and curr2 and curr2.next:
        while curr2 and curr2.next:
            curr1 = curr1.next
            curr2 = curr2.next.next
            if curr1 is curr2:
                return True
        return False


# runtime 40 ms, 80%; memory 18.1 MB, 57%
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        a = b = head
        while b and b.next:
            a = a.next
            b = b.next.next
            if a is b:
                return True
        return False

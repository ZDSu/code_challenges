# https://leetcode.com/problems/swap-nodes-in-pairs/


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return

        if not head.next.next:
            prev = None
            head = head.next
            head.next = prev
            head = prev

        dummy = ListNode(None)
        dummy.next = head
        curr = dummy.next

        def recurse(node1, node2):
            if not node1 or not node2:
                return
            if head is node1:
                dummy.next = node2
            temp = node2.next
            node1, node2 = node2, node1
            node1.next = node2
            node2.next = temp
            # next = node2.next
            # prev = None
            # temp = node2
            # curr.next = prev
            # prev = curr
            # curr = temp
            # curr.next.next = 
            recurse(node2.next, node2.next.next) 

        recurse(curr, curr.next)
        return dummy.next

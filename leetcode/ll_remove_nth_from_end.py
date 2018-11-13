# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
# https://leetcode.com/articles/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return []

        curr1 = curr2 = head
        m = n
        while curr1 and n > 0:
            if curr1.next:
                curr1 = curr1.next
            n -= 1
        if not curr1.next:
            return curr1
        while curr1 and curr1.next and m > 0:
            curr1 = curr1.next
            curr2 = curr2.next
            m -= 1
        curr2.next = curr2.next.next
        return head

# above code doesn't pass last test case below
# test cases: 
# [1], 1  returns []
# [1,2], 2  returns [2]
# [1,2], 1  returns [1]


# from solution #2 on leetcode:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        curr1 = curr2 = dummy
        for _ in range(1, n + 2):
            curr1 = curr1.next
        while curr1:
            curr1 = curr1.next
            curr2 = curr2.next
        curr2.next = curr2.next.next
        return dummy.next
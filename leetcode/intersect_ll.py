# https://leetcode.com/problems/intersection-of-two-linked-lists/description/
# https://leetcode.com/articles/intersection-of-two-linked-lists/


# passes 39/42 tests. time limit exceeded for long test cases

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return
        
        listA = []
        curr = headA
        while curr:
            listA.append(curr)
            curr = curr.next
        
        curr = headB
        while curr:
            if curr in listA:
                return curr
            curr = curr.next      


# changing listA array to use set instead passes all tests
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return
        
        listA = set()
        curr = headA
        while curr:
            listA.add(curr)
            curr = curr.next
        
        curr = headB
        while curr:
            if curr in listA:
                return curr
            curr = curr.next

# test cases:
# [] []
# [1] [1]

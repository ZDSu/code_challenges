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

# test case:  no intersection
# 0
# [1,3]
# [2,4]
# 2
# 2


# (solution 3)
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

        currA = headA
        currB = headB

        while currA != currB:
            if not currA:
                currA = headB
            else:
                currA = currA.next
            if not currB:
                currB = headA
            else:
                currB = currB.next
        return currA


# (solution 2)
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
        
        listA = set()
        while headA:
            listA.add(headA)
            headA = headA.next
        
        while headB:
            if headB in listA:
                return headB
            headB = headB.next
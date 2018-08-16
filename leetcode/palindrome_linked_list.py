# https://leetcode.com/problems/palindrome-linked-list/description/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = slow = head

        # get to middle node
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # in-place reversal of second half
        previous = None
        while slow:
            temp = slow.next
            slow.next = previous
            previous = slow
            slow = temp
        
        # compare first and second halves
        while previous:
            if previous.val != head.val:
                return False
            previous = previous.next
            head = head.next
        return True


# solution that fails 1 test with Time Limit Exceeded
class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        list2 = []
        current = head
        while current:
            list2 = [current.val] + list2
            current = current.next

        return list2 == list2[::-1]
        
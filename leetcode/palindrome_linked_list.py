# https://leetcode.com/problems/palindrome-linked-list/description/
# fails 1 test with Time Limit Exceeded

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
        list2 = []
        current = head
        while current is not None:
            list2 = [current.val] + list2
            current = current.next

        return list2 == list2[::-1]
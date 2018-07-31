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

        current = head
        for i in range(len(list2) // 2):
            if current.val != list2[i]:
                return False
            current = current.next
        return True
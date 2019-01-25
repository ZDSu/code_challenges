# https://leetcode.com/problems/palindrome-linked-list/description/


# 76 ms, 96%
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


# 72 ms, 100% (but not O(N) time or O(1) space)
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
        if not head:
            return True

        values = []
        while head:
            values.append(head.val)
            head = head.next
        j = len(values) - 1
        for i in range(len(values) // 2):
            if values[i] != values[j]:
                return False
            j -= 1
        return True
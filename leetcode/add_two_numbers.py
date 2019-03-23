# https://leetcode.com/problems/add-two-numbers/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        print(l1.val, l2.val)
        num1 = num2 = ''

        while l1 and l2:
            num1 = str(l1.val) + num1
            num2 = str(l2.val) + num2
            l1, l2 = l1.next, l2.next
        total = str(int(num1) + int(num2))
        l3 = ListNode(0)
        l3 = l3.next
        for i in range(len(total)-1, -1, -1):
            l3 = ListNode(int(total[i]))
            l3 = l3.next
        return l3

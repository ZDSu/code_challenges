# https://leetcode.com/problems/add-two-numbers/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# passes 729/1563 tests; assumed length of l1 and l2 would be same (did not indicate either way)
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = num2 = ''

        while l1 and l2:
            num1 = str(l1.val) + num1
            num2 = str(l2.val) + num2
            l1, l2 = l1.next, l2.next
        total = str(int(num1) + int(num2))
        
        l3 = ListNode(int(total[-1]))
        dummy = ListNode(0)
        dummy.next = l3
        for i in range(len(total)-2, -1, -1):
            l3.next = ListNode(int(total[i]))
            l3 = l3.next
            
        return dummy.next

# test case: [1,8], [0]   returns [1,8]

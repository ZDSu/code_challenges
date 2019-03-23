# https://leetcode.com/problems/add-two-numbers/

# instuctions should clarify that l1 and l2 can have different lengths

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# runtime: 120 ms, 34%; memory 13.4 MB, 5%
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = num2 = ''

        while l1:
            num1 = str(l1.val) + num1
            l1 = l1.next
        while l2:
            num2 = str(l2.val) + num2
            l2 = l2.next
        total = str(int(num1) + int(num2))

        l3 = ListNode(int(total[-1]))
        dummy = ListNode(0)
        dummy.next = l3
        for i in range(len(total)-2, -1, -1):
            l3.next = ListNode(int(total[i]))
            l3 = l3.next

        return dummy.next


# runtime: 120 ms, 34%; memory 13.3 MB, 5%
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = num2 = ''

        while l1 or l2:
            if l1:
                num1 = str(l1.val) + num1
                l1 = l1.next
            if l2:
                num2 = str(l2.val) + num2
                l2 =  l2.next
        total = str(int(num1) + int(num2))

        l3 = ListNode(int(total[-1]))
        dummy = ListNode(0)
        dummy.next = l3
        for i in range(len(total)-2, -1, -1):
            l3.next = ListNode(int(total[i]))
            l3 = l3.next

        return dummy.next

# test case: [1,8], [0]   returns [1,8]

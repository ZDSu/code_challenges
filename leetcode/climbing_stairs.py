# https://leetcode.com/problems/climbing-stairs/
# https://leetcode.com/articles/climbing-stairs/


# runtime 12 ms, 95%; memory 11.7 MB, 56%
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1 or n == 2:
            return n

        a = 1
        b = 2
        for _ in range(3, n + 1):
            temp = a + b
            a = b
            b = temp
        return temp

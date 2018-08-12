# https://leetcode.com/problems/reverse-integer/
# https://leetcode.com/articles/reverse-integer/


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x = str(x)
        result = 0
        if x[0] == '-':
            result = int('-' + x[-1:0:-1])
        else:
            result = int(x[-1:0:-1] + x[0])

        if result > 2**31 - 1 or result < -2**31 + 1:
            result = 0
        return result
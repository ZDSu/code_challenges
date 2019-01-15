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


# test case: 1534236469   returns 0


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        digit = list(str(x))
        digit.reverse()
        rev = ''
        for char in digit:
            if char == '-':
                rev = char + rev
            else:
                rev += char
        rev = int(rev)
        if rev > 2**31 - 1 or rev < -2**31:
            return 0
        return rev


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x = str(x)
        if x[0] == '-':
            x = int(x[0] + x[-1:0:-1])
        else:
            x = int(x[::-1])
        if x > 2**31 - 1 or x < -2**31:
            return 0
        return x


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = ''
        x = str(x)
        if x[0] == '-':
            res += '-'
        for i in range(len(x)-1, -1, -1):
            if x[i] == '-':
                continue
            res += x[i]
        if int(res) > 2**31 - 1 or int(res) < -2**31:
            return 0
        return int(res)
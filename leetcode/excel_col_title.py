# https://leetcode.com/problems/excel-sheet-column-title/


class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        # n // 351
        # if n > 702:
        res = ''

        if n < 27:
            return chr(n + 64)
        else:
            res += chr((n // 26) + 64)
            res += chr((n % 26) + 64)
            return res


# test case: 
# 24568  returns "AJHX"
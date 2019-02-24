# https://leetcode.com/problems/excel-sheet-column-number/


# runtime: 28 ms, 74%; memory: 10.7 MB, 51%
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        for letter in s:
            res *= 26
            res += ord(letter) - 64
        return res

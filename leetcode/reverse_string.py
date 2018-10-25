# https://leetcode.com/problems/reverse-string/description/


class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s
        rev = ''
        for char in reversed(s):
            rev += char
        return rev


class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]
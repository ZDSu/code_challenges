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


# solution 1 = 68 ms; solution 2 = 48 ms; solution 3 = 204 ms
# not very performant solution
class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s
        
        rev = ''
        for char in s:
            rev = char + rev
        return rev
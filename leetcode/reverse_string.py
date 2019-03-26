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


# runtime: 200 ms, 29%; memory: 18.5 MB, 1%
# runtime: 180ms, 50%; memory 17.6 MB, 11%
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: void Do not return anything, modify s in-place instead.
        """
        i = 0
        j = len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1


# recursive method
# runtime: 232 ms, 12%; memory: 41.9 MB, 1%
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: void Do not return anything, modify s in-place instead.
        """
        def recurse(start, stop, string):
            if start >= stop:
                return

            string[start], string[stop] = string[stop], string[start]
            recurse(start + 1, stop - 1, string)

        recurse(0, len(s) - 1, s)

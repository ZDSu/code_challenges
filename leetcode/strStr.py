# https://leetcode.com/problems/implement-strstr/


class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == '':
            return 0
        if needle in haystack:
            return haystack.find(needle)
        return -1


# or in one line:
return haystack.find(needle)


# 32 ms, 100%
class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0

        length = len(needle)
        i = 0

        while i + length <= len(haystack):
            if haystack[i:i + length] == needle:
                return i
            i += 1
        return -1


# 52 ms, 45%
class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0

        for i in range(len(haystack)):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
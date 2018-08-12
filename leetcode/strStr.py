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
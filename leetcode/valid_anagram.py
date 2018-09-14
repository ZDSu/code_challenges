# https://leetcode.com/problems/valid-anagram/description/
# https://leetcode.com/articles/valid-anagram/


class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        s = list(s)
        for char in t:
            if char in s:
                s.remove(char)
            else:
                return False
        if len(s) > 0:
            return False
        return True
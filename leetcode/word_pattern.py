# https://leetcode.com/problems/word-pattern/description/


class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        pairs = {}
        str = str.split(' ')
        if len(pattern) != len(str):
            return False
        
        for i in range(len(pattern)):
            if pattern[i] in pairs:
                if str[i] != pairs[pattern[i]]:
                    return False
            elif str[i] in pairs.values():
                return False
            pairs[pattern[i]] = str[i]
        return True
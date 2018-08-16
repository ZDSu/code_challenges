# https://leetcode.com/problems/backspace-string-compare/description/
# https://leetcode.com/articles/backspace-string-compare/


class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        sstring = ''
        tstring = ''
        
        for char in S:
            if char != '#':
                sstring += char
            else:
                sstring = sstring[:-1]
        
        for char in T:
            if char != '#':
                tstring += char
            else:
                tstring = tstring[:-1]
        
        return sstring == tstring
# https://leetcode.com/problems/length-of-last-word/description/


class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        
        words = s.split(' ')
        return len(words[-1])


# test cases
# ''  returns 0
# 'a '  returns 1
# 'b   a    '  returns 1


class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        words = s.strip().split()
        if not words:
            return 0
        return len(words[-1])


class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        word = ''
        if not s:
            return 0

        s = s.rstrip()
        for i in range(len(s)-1, -1, -1):
            if s[i] == ' ':
                break
            word += s[i]
        return len(word)
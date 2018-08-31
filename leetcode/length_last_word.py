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
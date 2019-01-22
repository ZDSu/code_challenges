# https://leetcode.com/problems/palindrome-number/description/
# solution: https://leetcode.com/articles/palindrome-number/

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        backwards = str(x)[::-1]
        if x == int(backwards):
            return True
        else:
            return False


class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        
        x = str(x)
        j = len(x) - 1
        for i in range(len(x) // 2):
            if x[i] != x[j]:
                return False
            j -= 1
        return True


# test case: 11   returns True
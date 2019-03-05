# https://leetcode.com/problems/valid-palindrome/description/


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = re.sub('[^A-Za-z0-9]+', '', s).lower()
        return s == s[::-1]


# iteratively, better solution
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = re.sub('[^A-Za-z0-9]+', '', s).lower()

        i = 0
        j = len(s) - 1

        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True


# doesn't pass test case ".," (see below)
class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True

        s = s.strip().lower()
        letters = set(['a','b','c','d','e','f','g','h','i','j','k','l','m','n', 'o','p','q','r','s','t','u', 'v','w','x','y','z'])
        # letters = 'abcdefghijklmnopqrstuvwxyz'
        # letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n', 'o','p','q','r','s','t','u', 'v','w','x','y','z']
        i = 0
        j = len(s) - 1

        while i < j:
            while s[i] not in letters:
                i += 1
            while s[j] not in letters:
                j -= 1
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True


# test case: ".,"  running code with this as a custom testcase says should output True... why? same result for ".a,"   these are not empty strings!

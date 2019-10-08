# https://leetcode.com/problems/valid-palindrome-ii/description/
# https://leetcode.com/articles/valid-palindrome-ii


# solution passes all but 2 test cases
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 0
        j = len(s) - 1
        delete = 1

        while i < j:
            if s[i] != s[j]:
                if s[i + 1] == s[j] and delete:
                    delete -= 1
                    i += 1
                elif s[i] == s[j-1] and delete:
                    delete -= 1
                    j -= 1
                else:
                    return False
            i += 1
            j -= 1
        return True

# test cases:
# 'aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga'
# "tcaac"  [when switched lines 19 and 22, only passes 268/460 tests cases]

# (my own test case) 'aguokepatgbnvfqmgmlucupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuclmgmqfvnbgtapekouga'

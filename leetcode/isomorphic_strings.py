# https://leetcode.com/problems/isomorphic-strings/description/


class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        pairs = {}
        for i in range(len(s)):
            if s[i] in pairs:
                if t[i] != pairs[s[i]]:
                    return False
            elif t[i] in pairs.values():
                return False
            pairs[s[i]] = t[i]
        return True


# test cases:
# "ab" "aa"
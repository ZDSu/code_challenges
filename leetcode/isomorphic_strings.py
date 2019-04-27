# https://leetcode.com/problems/isomorphic-strings/description/


# runtime 44 ms, 84%; memory 13.4 MB, 16%
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


# runtime 40 ms, 96%; memory 13.5 MB, 16%
class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        pairs = {}
        keys = set()

        for i in range(len(s)):
            if s[i] in pairs:
                if pairs[s[i]] != t[i]:
                    return False
            else:
                if t[i] in keys:
                    return False
                pairs[s[i]] = t[i]
                keys.add(t[i])
        return True


# test cases:
# "ab" "aa"

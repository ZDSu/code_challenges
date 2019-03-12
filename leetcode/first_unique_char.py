# https://leetcode.com/problems/first-unique-character-in-a-string/description/
# https://leetcode.com/articles/first-unique-character-in-a-string/


class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return -1
        singles = {}
        doubles = {}
        for i in range(len(s)):
            if s[i] in doubles:
                doubles[s[i]] += 1
            elif s[i] in singles:
                doubles[s[i]] = 2
                del singles[s[i]]
            else:
                singles[s[i]] = i
        if not singles:
            return -1
        key_min = min(singles.keys(), key = lambda k: singles[k])
        return singles[key_min]


# test case: ''   returns -1


# solution method (but not using counter objects)
# runtime 164 ms, 35%; memory 13.4 MB, 5%
class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return -1

        letters = {}
        for i in range(len(s)):
            if s[i] in letters:
                letters[s[i]] += 1
            else:
                letters[s[i]] = 1
        for i in range(len(s)):
            if letters[s[i]] == 1:
                return i
        return -1


# runtime 164 ms, 35%; memory 13.4 MB, 5%
class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return -1

        chars = {}

        for i in range(len(s)):
            if s[i] in chars:
                chars[s[i]] += 1
            else:
                chars[s[i]] = 1

        for i in range(len(s)):
            if chars[s[i]] == 1:
                return i

        return -1


# solution method
# runtime 108 ms, 80%; memory 13.2 MB, 5%
class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return -1

        chars = collections.Counter(s)

        for i in range(len(s)):
            if chars[s[i]] == 1:
                return i

        return -1

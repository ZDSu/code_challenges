# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# https://leetcode.com/problems/longest-substring-without-repeating-characters/solution/


# runtime 640 ms, 12.5%; memory 13.1 MB, 5.5%
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        i = longest = 0
        chars = {}

        while i <= len(s) - 1:
            if s[i] not in chars:
                chars[s[i]] = i
            else:
                if len(chars) > longest:
                    longest = len(chars)
                temp = chars[s[i]] + 1
                chars = {}
                chars[s[temp]] = temp
                i = temp
            i += 1
        if len(chars) > longest:
            longest = len(chars)
        return longest


# runtime 56 ms, 99.5%; memory 13.3 MB, 5%
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        ls = ''
        longest = 0
        for char in s:
            if char in ls:
                if len(ls) > longest:
                    longest = len(ls)
                ls = ls[ls.index(char) + 1:]
            ls += char
        if len(ls) > longest:
            longest = len(ls)
        return longest


# runtime 48 ms, 100%; memory 13.3 MB, 5%
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        start = -1
        max = 0
        for i in range(len(s)):
            if s[i] in d and d[s[i]] > start:
                start = d[s[i]]
                d[s[i]] = i

            else:
                d[s[i]] = i
                if i - start > max:
                    max = i - start
        return max


# test cases:  "au", "dvdf"

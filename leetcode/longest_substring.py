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

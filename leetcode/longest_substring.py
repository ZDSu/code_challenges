# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# https://leetcode.com/problems/longest-substring-without-repeating-characters/solution/



class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        longest = curr = 0
        chars = set()

        for char in s:
            if char in chars:
                if curr > longest:
                    longest = curr
                curr = 1
                chars = set(char)
            else:
                chars.add(char)
                curr += 1
        if curr > longest:
            return curr
        return longest

# https://leetcode.com/problems/reverse-vowels-of-a-string/submissions/


class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowels = {'a', 'e', 'i', 'o', 'u'}
        j = len(s) - 1
        for i in range(len(s)):
            if s[i] in vowels:
                while j > i:
                    if s[j] in vowels:
                        s[i], s[j] = s[j], s[i]
                        j -= 1
                        continue
                    j -= 1

        return ''.join(s)

# testcase: "aA"  returns "Aa"

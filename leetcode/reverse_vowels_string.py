# https://leetcode.com/problems/reverse-vowels-of-a-string/submissions/


# runtime 56 ms, 100%; memory 14.3 MB, 19%
class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] not in vowels:
                i += 1
                continue
            if s[j] not in vowels:
                j -= 1
                continue
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1

        return ''.join(s)


# runtime 68 ms, 71%; memory 14 MB, 23%
class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] not in vowels:
                i += 1
                continue
            else:
                while s[j] not in vowels:
                    j -= 1
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1

        return ''.join(s)


# testcases:
# "aA"  returns "Aa"
# "race car"   returns "race car"

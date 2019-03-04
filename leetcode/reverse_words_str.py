# https://leetcode.com/problems/reverse-words-in-a-string/


# runtime: 40 ms, 100%; memory 13.3 MB, 100%
class Solution:
    def reverseWords(self, s: str) -> str:
        if not s:
            return ''

        res = ''
        s = s.split(' ')
        for word in s:
            if word:
                res = f'{word} {res}'
        return res[:-1].strip()

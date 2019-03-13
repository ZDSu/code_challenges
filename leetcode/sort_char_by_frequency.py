# https://leetcode.com/problems/sort-characters-by-frequency/


# runtime 48 ms, 76%; memory 13.7 MB, 17%
class Solution:
    def frequencySort(self, s: str) -> str:
        if not s:
            return ''

        res = ''
        count = collections.Counter(s).most_common()

        for item in count:
            res += item[0] * item[1]

        return res

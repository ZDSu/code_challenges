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


# runtime 64 ms, 41%; memory 13.6 MB, 17%
class Solution:
    def frequencySort(self, s: str) -> str:
        res = ''
        count = {}

        for char in s:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1

        for item in sorted(count.items(), key=lambda x: x[1], reverse=True):
            res += item[0] * item[1]

        return res

# https://leetcode.com/problems/jewels-and-stones/
# https://leetcode.com/problems/jewels-and-stones/solution/

# runtime 40 ms, 43%; memory 13.9 MB, 5%
# runtime 32 ms, 93%; memory 13.8 MB, 5%
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewels = set(J)
        res = 0

        for stone in S:
            if stone in jewels:
                res += 1

        return res

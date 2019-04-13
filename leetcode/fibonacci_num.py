# https://leetcode.com/problems/fibonacci-number/submissions/


# runtime 36 ms, 79%; memory 13.4 MB, 5%
class Solution:
    def fib(self, N: int) -> int:
        if N == 0:
            return 0
        if N == 1:
            return 1

        one = 0
        two = 1
        res = 0
        for _ in range(2, N + 1):
            res = one + two
            one = two
            two = res
        return res

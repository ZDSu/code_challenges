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


# runtime 36 ms, 79%; memory 13.2 MB, 5%
class Solution:
    def fib(self, N: int) -> int:
        if N == 0 or N == 1:
            return N

        one = 0
        two = 1
        for _ in range(2, N + 1):
            temp = one + two
            one = two
            two = temp
        return two


# runtime 36 ms, 79%; memory 13.1 MB, 5%
class Solution:
    def fib(self, N: int) -> int:
        if N == 0:
            return 0
        if N == 1:
            return 1

        one = 0
        two = 1
        for _ in range(2, N + 1):
            temp = one + two
            one = two
            two = temp
        return two


# supposed to be 100% solution but got same results as my solutions
# runtime 36 ms, 79%; memory 13.3 MB, 5%
class Solution:
    def fib(self, N: 'int') -> 'int':
        if N == 0: return 0
        if N == 1: return 1
        i = 2
        fn0, fn1 = 0, 1
        while(i <= N):
            t = fn1
            fn1 = fn1 + fn0
            fn0 = t
            i = i + 1
        return fn1


# recursive solution
# runtime 1304 ms, 5%; memory 13.3 MB, 5%
class Solution:
    def fib(self, N: int) -> int:
        if N == 0 or N == 1:
            return N
        return self.fib(N - 1) + self.fib(N - 2)


# runtime 16 ms, 90%; memory 11.8 MB, 22%
class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 0 or N == 1:
            return N

        first = 0
        second = 1
        for i in range(2, N + 1):
            next = first + second
            first = second
            second = next
        return next

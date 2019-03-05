# https://leetcode.com/problems/rotate-string/
# https://leetcode.com/articles/rotate-string/


# runtime: 52 ms, 22%; memory: 13.2 MB, 6%
class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        if not A and not B:
            return True

        for i in range(len(B)):
            if B[i] == A[0]:
                temp = f'{B[i:]}{B[:i]}'
                if A == temp:
                    return True
        return False


# runtime: 36 ms, 63%; memory 13.1 MB, 6%
class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if A == B:
            return True

        for i in range(len(A)):
                A = A[1:] + A[0]
                if A == B:
                    return True
        return False


# runtime: 52 ms, 22%; memory: 13.2 MB, 6%
class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        return len(A) == len(B) and B in A + A


# runtime: 36 ms, 63%; memory 13.1 MB, 6%
class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        if A in B * 2:
            return True
        return False


# test cases: 
# "abcde", "cdeab"  returns True
# "", "a"  returns False
# "bbbacddceeb", "ceebbbbacdd"  returns True

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

# test cases: 
# "abcde", "cdeab"  returns True
# "", "a"  returns False
# "bbbacddceeb", "ceebbbbacdd"  returns True

# https://leetcode.com/problems/rotate-string/
# https://leetcode.com/articles/rotate-string/


class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False

        for i in range(len(B)):
            if B[i] == A[0]:
                B = f'{B[i:]}{B[:i]}'
                if A == B:
                    return True
        return False

# test cases: 
# "abcde", "cdeab"  returns True
# "", "a"  returns False
# "bbbacddceeb", "ceebbbbacdd"  returns True

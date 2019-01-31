# https://leetcode.com/problems/string-without-aaa-or-bbb/
# https://leetcode.com/articles/string-without-aaa-or-bbb/solution/


class Solution:
    def strWithout3a3b(self, A, B):
        """
        :type A: int
        :type B: int
        :rtype: str
        """
        res = ''
        while A and B:
            if not res or res[-1] != 'a':
                if A >= 2:
                    res += 'aa'
                    A -= 2
                elif A == 1:
                    res += 'a'
                    A -= 1
            if not res or res[-1] != 'b':
                if B >= 2:
                    res += 'bb'
                    B -= 2
                elif B == 1:
                    res += 'b'
                    B -= 1
        while A or B:
            if A and res[-1] != 'a':
                if A >= 2:
                    res += 'aa'
                    A -= 2
                elif A == 1:
                    res += 'a'
                    A -= 1
            if B and res[-1] != 'b':
                if B >= 2:
                    res += 'bb'
                    B -= 2
                elif B == 1:
                    res += 'b'
                    B -= 1
        return res
# https://leetcode.com/problems/roman-to-integer/description/


class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        romans = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        total = 0
        iter = 0
        while iter < len(s) - 1:
            if s[iter] == 'I':
                if s[iter + 1] == 'V':
                    total += 4
                    iter += 2
                elif s[iter + 1] == 'X':
                    total += 9
                    iter += 2
                else:
                    total += 1
                    iter += 1
            elif s[iter] == 'X':
                if s[iter + 1] == 'L':
                    total += 40
                    iter += 2
                elif s[iter + 1] == 'C':
                    total += 90
                    iter += 2
                else:
                    total += 10
                    iter += 1
            elif s[iter] == 'C':
                if s[iter + 1] == 'D':
                    total += 400
                    iter += 2
                elif s[iter + 1] == 'M':
                    total += 900
                    iter += 2
                else:
                    total += 100
                    iter += 1
            elif s[iter] == 'M':
                total += 1000
                iter += 1
            else:
                total += romans[s[iter]]
                iter += 1
        if iter == len(s) - 1:
            total += romans[s[-1]]
        return total


# another solution
        # dic={'I':1,
        #      'V':5,
        #      'X':10,
        #      'L':50,
        #      'C':100,
        #      'D':500,
        #      'M':1000}
        # sum = 0
        # for i in range(len(s)):
        #     if i == 0 or dic[s[i]] <= dic[s[i-1]]:
        #         sum += dic[s[i]]
        #     else:
        #         sum += dic[s[i]] - 2 * dic[s[i-1]]
        # return sum


class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        romans = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        num = 0

        for i in range(len(s) - 1):
            if romans[s[i]] < romans[s[i + 1]]:
                num -= romans[s[i]]
            else:
                num += romans[s[i]]
        return num + romans[s[-1]]
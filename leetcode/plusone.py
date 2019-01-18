# https://leetcode.com/problems/plus-one/description/


# (44 ms)
class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        number = ''
        plus = []
        for each in digits:
            number += str(each)
        number = str(int(number) + 1)
        for each in number:
            plus.append(int(each))
        return plus


# using recursion (48 ms)
class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits[-1] == 9:
            if len(digits) == 1:
                return [1, 0]
            return self.plusOne(digits[:-1]) + [0]
        else:
            digits[-1] += 1
        return digits


# (36 ms)
class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in range(len(digits)-1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
                if i == 0:
                    digits.insert(0, 1)
        return digits


class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if not digits:
            return [1]

        if digits[-1] != 9:
            digits[-1] += 1
        else:
            for i in range(len(digits)-1, -1, -1):
                if digits[i] == 9:
                    digits[i] = 0
                    if i == 0:
                        digits.insert(0, 1)
                else:
                    digits[i] += 1
                    break
        return digits


# test case: [9] returns [1,0]
# https://leetcode.com/problems/plus-one/description/


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
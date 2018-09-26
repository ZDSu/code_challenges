# https://leetcode.com/problems/fizz-buzz/description/
# https://leetcode.com/articles/fizz-buzz/


class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        for num in range(1, n + 1):
            if num % 15 == 0:
                result.append('FizzBuzz')
            elif num % 3 == 0:
                result.append('Fizz')
            elif num % 5 == 0:
                result.append('Buzz')
            else:
                result.append(str(num))
        return result
# https://leetcode.com/problems/generate-parentheses/description/
# https://leetcode.com/articles/generate-parentheses/
# https://www.geeksforgeeks.org/print-all-combinations-of-balanced-parentheses/


# first two are based on Dave S's solution:
class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []

        def recurse(count, right, final, current):
            if count == 0:
                result.append(current)
                return
            if count > right:
                recurse(count - 1, right + 1, result, current + '(')
            if right > 0:
                recurse(count - 1, right - 1, result, current + ')')

        recurse(n * 2, 0, result, '')
        return result


class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        
        def recurse(count, open, current):
            if count == 0:
                result.append(current)
                return
            if count > open:
                recurse(count - 1, open + 1, current + '(')
            if open > 0:
                recurse(count - 1, open - 1, current + ')')
        
        recurse(n*2, 0, '')
        return result


# next 2 are based on solution #2
class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        
        def recurse(open, close, current):
            if open == n and close == 0:
                result.append(current)
                return
            if open < n:
                recurse(open + 1, close + 1, current + '(')
            if close:
                recurse(open, close - 1, current + ')')
        
        recurse(0,0,'')
        return result


class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        
        def recurse(open, close, current):
            if open == 0 and close == 0:
                result.append(current)
                return
            if open:
                recurse(open - 1, close + 1, current + '(')
            if close:
                recurse(open, close - 1, current + ')')
        
        recurse(n,0,'')
        return result


# based on geeks for geeks solution
class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        
        def recurse(open=0, close=0, current=''):
            if open == n and close == n:
                result.append(current)
            if open < n:
                recurse(open + 1, close, current +'(')
            if open > close:
                recurse(open, close + 1, current + ')')
        
        recurse()
        return result
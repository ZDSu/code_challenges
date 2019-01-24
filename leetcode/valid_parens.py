# https://leetcode.com/problems/valid-parentheses/
# https://leetcode.com/articles/valid-parentheses/


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == '':
            return True
        
        open = ''
        for each in s:
            if each == '(' or each == '{' or each == '[':
                open += each
            elif each == ')':
                if len(open) == 0:
                    return False
                elif open[-1] == '(':
                    open = open[:-1]
                else:
                    return False
            elif each == '}':
                if len(open) == 0:
                    return False
                elif open[-1] == '{':
                    open = open[:-1]
                else:
                    return False
            else:
                if len(open) == 0:
                    return False
                elif open[-1] == '[':
                    open = open[:-1]
                else:
                    return False
        if len(open) > 0:
            return False
        return True


# test cases:  '[', '}' and examples


# another solution (with help from dicussion); has longer runtime but less lines of code
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 == 0:
            for i in range(len(s) // 2):
                s = s.replace("()", "")
                s = s.replace("{}", "")
                s = s.replace("[]", "")
            if s == "":
                return True
        return False


# hash solution from newly written solution article
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        parens = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        stack = []
        
        for char in s:
            if char in parens and stack:
                if stack[-1] == parens[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        return not stack


# 100%, 32 ms
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        
        if len(s) % 2 == 1:
            return False
        
        left = '{[('
        temp = ''
        
        for char in s:
            if char in left:
                temp += char
            elif char == '}':
                if not temp or temp[-1] != '{':
                    return False
                if temp[-1] == '{':
                    temp = temp[:-1]
            elif char == ']':
                if not temp or temp[-1] != '[':
                    return False
                if temp[-1] == '[':
                    temp = temp[:-1]
            elif char == ')':
                if not temp or temp[-1] != '(':
                    return False
                if temp[-1] == '(':
                    temp = temp[:-1]
        if temp:
            return False
        return True


#  97%, 36 ms [just took out unnecessary if conditional from above code so not sure why it takes longer]
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True

        if len(s) % 2 == 1:
            return False

        left = '{[('
        temp = ''

        for char in s:
            if char in left:
                temp += char
            elif char == '}':
                if not temp or temp[-1] != '{':
                    return False
                temp = temp[:-1]
            elif char == ']':
                if not temp or temp[-1] != '[':
                    return False
                temp = temp[:-1]
            elif char == ')':
                if not temp or temp[-1] != '(':
                    return False
                temp = temp[:-1]
        if temp:
            return False
        return True
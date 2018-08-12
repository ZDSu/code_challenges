# https://leetcode.com/problems/valid-parentheses/


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
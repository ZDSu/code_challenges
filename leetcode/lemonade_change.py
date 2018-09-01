# https://leetcode.com/problems/lemonade-change/description/
# solution: https://leetcode.com/articles/lemonade-change/


class Solution:
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        cash = {'five': 0, 'ten': 0, 'twenty': 0}
        
        for each in bills:
            if each == 5:
                cash['five'] += 1
            elif each == 10:
                if cash['five'] < 1:
                    return False
                cash['ten'] += 1
                cash['five'] -= 1
            else:
                if cash['five'] < 3 and (cash['five'] < 1 or cash['ten'] < 1):
                    return False
                if cash['ten'] > 0 and cash['five'] > 0:
                    cash['ten'] -= 1
                    cash['five'] -= 1
                else:
                    cash['five'] -= 3
                cash['twenty'] += 1
        return True


# from solution, takes half the runtime
class Solution:
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        five = ten = 0
        for each in bills:
            if each == 5:
                five += 1
            elif each == 10:
                if not five: 
                    return False
                five -= 1
                ten += 1
            else:
                if ten and five:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True
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
# 44 ms, 6.8 MB, 100%
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


# 44 ms, 6.8 MB, 100% (someone else's solution)
class Solution:
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        five = ten = 0
        for num in bills:
            if num == 5:
                five += 1
            elif num == 10 and five:
                ten += 1
                five -= 1
            elif num == 20 and five and ten:
                five -= 1
                ten -= 1
            elif num == 20 and five >= 3:
                five -= 3
            else:
                return False
        return True


# 48 ms, 6.9 MB, 75%
class Solution:
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        money = {5: 0, 10: 0, 20: 0}

        for bill in bills:
            if bill == 5:
                money[5] += 1
            elif bill == 10:
                if money[5] > 0:
                    money[5] -= 1
                    money[10] += 1
                else:
                    return False
            else:  # bill == 20:
                if money[5] > 0 and money[10] > 0:
                    money[10] -= 1
                    money[5] -= 1
                elif money[5] > 2:
                    money[5] -= 3
                else:
                    return False
                money[20] += 1
        return True

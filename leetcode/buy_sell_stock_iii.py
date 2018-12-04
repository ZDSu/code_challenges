# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/description/


# passes 189/200 test cases
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        
        profit = []
        low = prices[0]
        high = None
        
        for i in range(1, len(prices)):
            if prices[i] <= prices[i - 1]:
                if high:
                    profit.append(high - low)
                    high = None
                low = prices[i]
            else:
                high = prices[i]
        if high:
            profit.append(high - low)
                    
        profit.sort()
        if len(profit) > 1:
            return profit[-1] + profit[-2]
        elif len(profit) == 1:
            return profit[0]
        else:
            return 0


# test case:
# [1,2,3,4,5]  returns 4
# [1,2,4,2,5,7,2,4,9,0] returns 13 (code above returns 12, so not passing this test case)
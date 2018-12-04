# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/
# https://leetcode.com/articles/best-time-to-buy-and-sell-stock-ii/


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        
        low = prices[0]
        high = None
        profit = 0
        
        for i in range(1, len(prices)):
            if prices[i] < prices[i - 1]:
                if high:
                    profit += high - low
                    high = None
                low = prices[i]
            else:
                if not high or prices[i] > high:
                    high = prices[i]

        if high:
            profit += high - low
        return profit


# based on solution 3  (same runtime as above solution)
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i-1]
        return profit
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
# https://leetcode.com/articles/best-time-to-buy-and-sell-stock/
# https://www.programcreek.com/2014/02/leetcode-best-time-to-buy-and-sell-stock-java/


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
        profit = None

        for i in range(1, len(prices)):
            if not high:
                if prices[i] < low:
                    low = prices[i]
                elif prices[i] > low:
                    high = prices[i]
                    if not profit:
                        profit = high - low
                    else:
                        profit = max([profit, (high - low)])
            else:
                if prices[i] > high:
                    high = prices[i]
                    profit = max([profit, (high - low)])
                if prices[i] < low:
                    low = prices[i]
                    high = None

        if not profit:
            return 0
        return profit

# test cases:
# [7,6,4,3,1] returns 0
# [] returns 0
# [2,4,1]  returns 2
# [2,1,2,1,0,1,2]  returns 2


# after reading solution
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        low = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] <= low:
                low = prices[i]
            elif prices[i] - low > profit:
                profit = prices[i] - low

        return profit
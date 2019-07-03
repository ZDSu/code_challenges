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


# runtime 52 ms, 52%; memory 12.6 MB, 51%
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        profit = 0
        low = prices[0]
        high = None

        for i in range(1, len(prices)):
            if prices[i] < low and not high:
                low = prices[i]
            elif prices[i] > high:
                high = prices[i]
            else:  # prices[i] < low and high
                profit += high - low
                low = prices[i]
                high = None
        if high:
            profit += high - low
        return profit


# based on solution 3
# runtime 48 ms, 77%; memory 12.6 MB, 67%
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


# based on solution 2
# runtime 44 ms, 91%; memory 12.5 MB, 83%
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        i = profit = 0
        while i < len(prices) - 1:
            while i < len(prices) - 1 and prices[i] >= prices[i+1]:
                i += 1
            low = prices[i]
            while i < len(prices) - 1 and prices[i] <= prices[i+1]:
                i += 1
            high = prices[i]
            profit += high - low
        return profit

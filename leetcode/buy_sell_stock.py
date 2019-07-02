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


# after reading solution
# runtime 60 ms, 32%; memory 12.7 MB, 26%
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


# runtime 48 ms, 80%; memory 12.5 MB, 70%
# runtime 44 ms, 90%; memory 12.6 MB, 44%
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        min = float('inf')

        for num in prices:
            if num < min:
                min = num
            elif num - min > profit:
                profit = num - min
        return profit


# runtime 40 ms, 95%; memory 12.6 MB, 42%
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

        for num in prices:
            if num < low:
                low = num
            elif num - low > profit:
                profit = num - low
        return profit


# runtime 40 ms, 99%; memory 12.6 MB, 42%
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        profit = 0
        curr = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < curr:
                curr = prices[i]
            else:
                if prices[i] - curr > profit:
                    profit = prices[i] - curr
        return profit


# test cases:
# [] returns 0
# [2,4,1]  returns 2
# [2,1,2,1,0,1,2]  returns 2

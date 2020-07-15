class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = max_profit = 0
        for price in range(len(prices)):
            max_profit = max(max_profit, prices[price] - prices[i])
            if prices[price] < prices[i]:
                i = price
        return max_profit
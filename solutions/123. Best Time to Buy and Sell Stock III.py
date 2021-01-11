# LeetCode Problem 123. Best Time to Buy and Sell Stock III (Python)
# Given an array for which the ith element is the price of a given stock on day i,
# return the maximum profit after at most two transactions

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
​
        # Forward Traversal: profits record the max profit by the ith day (transaction 1)
        profits = []
        max_profit = 0
        current_min = prices[0]
        for price in prices:
            current_min = min(current_min, price)
            max_profit = max(max_profit, price - current_min)
            profits.append(max_profit)
​
        # Backward Traversal: max_profit records the max profit after the ith day (transaction 2)
        total_max = 0    
        max_profit = 0
        current_max = prices[-1]
        for i in range(len(prices) - 1, -1, -1):
            current_max = max(current_max, prices[i])
            max_profit = max(max_profit, current_max - prices[i])
            total_max = max(total_max, max_profit + profits[i])
​
        return total_max

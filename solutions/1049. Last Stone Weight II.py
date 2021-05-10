class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        maxWeight = int(total / 2)
        dp = (maxWeight + 1) * [0]
        
        for stone in stones:
            for i in range(maxWeight, -1, -1):
                if i - stone >= 0:
                    dp[i] = max(stone + dp[i-stone], dp[i])
                    
        return total - 2 * dp[-1]

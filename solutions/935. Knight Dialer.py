class Solution:
    def knightDialer(self, n: int) -> int:
        d = {1:[6, 8], 2:[7, 9], 3:[4, 8], 4:[0, 3, 9], 5:[], 6:[0, 1, 7], 7:[2, 6], 8:[1, 3], 9:[2, 4], 0:[4, 6]}
        
        dp = [1] * 10
        for _ in range(n - 1):
            nxt = [0] * 10
            for i in range(10):
                for j in d[i]:
                    nxt[j] += dp[i]
            dp = nxt
        
        return sum(dp) % (10 ** 9 + 7)

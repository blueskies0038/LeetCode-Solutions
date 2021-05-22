class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        dp = [0] * (N+1)
        for a, b in trust:
            dp[a] -= 1
            dp[b] += 1
​
        for i in range(1, N+1):
            if dp[i] == N-1:
                return i
        return -1

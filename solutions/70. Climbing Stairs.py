class Solution:
    def climbStairs(self, n: int) -> int:
        a, b, sum = 0, 1, 0
        for _ in range(n):
            a, b, sum = b, a+b, sum+a
        return sum + 1
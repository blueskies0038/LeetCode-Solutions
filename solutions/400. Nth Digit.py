class Solution:
    def findNthDigit(self, n: int) -> int:
        digit = base = 1
        while n > 9*digit*base:
            n -= 9*digit*base
            digit += 1
            base *= 10
        quo, rem = divmod(n-1, digit)
        return int(str(base + quo)[rem])

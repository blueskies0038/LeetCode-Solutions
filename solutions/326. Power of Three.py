class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while n > 1 and n % 3 == 0:
            n /= 3
        if n == 1:
            return True
        return False

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for i in range(int(sqrt(c)) + 1):
            if int(sqrt(c-i**2))**2 + i**2 == c:
                return True
        return False

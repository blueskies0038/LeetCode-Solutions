class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num < 6:
            return False
        total = 1
        for i in range(2, int(sqrt(num)) + 1):
            if num%i == 0:
                total += i + num/i
        return total == num

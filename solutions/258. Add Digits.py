class Solution:
    def addDigits(self, num: int) -> int:
        num1 = 0
        while num > 9:
            num1 = num % 10
            num = num//10
            num = num + num1
        return num

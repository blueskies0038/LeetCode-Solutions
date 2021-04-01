class Solution:
    def convertToBase7(self, num: int) -> str:
        if not num:
            return "0"
        
        output = []
        negative = num < 0
        num = abs(num)
        
        while num > 0:
            digit = num % 7
            num //= 7
            output.append(str(digit))
​
        if negative:
            return "-" + ''.join(output[::-1])
        
        return ''.join(output[::-1])

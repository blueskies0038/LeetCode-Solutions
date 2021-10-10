class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0: return 1
        if n == 1: return 10
        output = 10
        choices = 9
        
        for i in range(1, n):
            choices = choices * (10 - i)   
            output += choices
        
        return output

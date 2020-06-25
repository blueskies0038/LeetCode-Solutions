class Solution:
    def reverse(self, x: int) -> int:
        min = -2**31
        max = 2**31 -1 
        if x >= 0:
            output = int(str(x)[::-1])
        else:
            output = -1 * int(str(-1*x)[::-1])
        if output not in range(min, max):
            output = 0
        return output
                
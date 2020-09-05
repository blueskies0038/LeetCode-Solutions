class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num <= 0: 
            return False
        if num == 1: 
            return True
        return int(math.log(num, 4)) == math.log(num, 4)

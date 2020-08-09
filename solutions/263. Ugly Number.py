class Solution:
    def isUgly(self, num: int) -> bool:
        if num == 0:
            return False
        ugly =[2,3,5]
        for i in ugly:
             while num % i == 0:
                    num /= i
        return num == 1 
​

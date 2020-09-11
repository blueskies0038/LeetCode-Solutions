class Solution:
    def isHappy(self, n: int) -> bool:
        square_sum = 0
        square_list = []
​
        while n != 1:
            square_sum += (n % 10)**2
            n //= 10
​
            if n < 10:
                square_sum += n**2
                n = square_sum
                
                if square_sum in square_list:
                    return False
                else:
                    square_list.append(square_sum)
                
                square_sum = 0
                
        return True

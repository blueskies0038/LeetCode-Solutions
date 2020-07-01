class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        least = 1
        most = x
        while least <= most:
            mid = least + (most - least)//2
            if mid*mid <= x:
                least = mid + 1
            else:
                most = mid - 1
        return least - 1
        
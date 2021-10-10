class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        start = 1
        end = num + 1
        
        while end >= start:
            mid = (start + end) // 2
            if mid**2 == num:
                return True
            elif mid**2 > num:
                end = mid - 1
            else:
                start = mid + 1
        return False

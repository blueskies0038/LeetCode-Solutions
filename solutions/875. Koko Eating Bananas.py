class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        left, right = 1, max(piles)
        while left < right:
            mid = (left + right) // 2
            time = sum([math.ceil(i/mid) for i in piles])
            if time > H:
                left = mid + 1
            else:
                right = mid
        return left

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        points = [0] * 10001
        prev = curr = 0
        for num in nums:
            points[num] += num
        for value in points:
            prev, curr = curr, max(prev + value, curr)
        return curr

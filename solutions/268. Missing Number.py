class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = actual = 0
        for i in range(len(nums)):
            actual += i
            total += nums[i]
        return actual - total + len(nums)

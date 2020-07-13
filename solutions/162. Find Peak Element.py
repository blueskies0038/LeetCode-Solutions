class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return nums.index(max(nums))
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1] and nums[i] > nums[i-1]:
                return i
                break
        return nums.index(max(nums))
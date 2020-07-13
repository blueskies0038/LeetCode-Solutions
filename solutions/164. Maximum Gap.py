class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        nums = sorted(nums)
        gap = nums[1] - nums [0]
        for i in range(0, len(nums) - 1):
            if nums[i+1] - nums[i] > gap:
                gap = nums[i+1] - nums[i]
        return gap
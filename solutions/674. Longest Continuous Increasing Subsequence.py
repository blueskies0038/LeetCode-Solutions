class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        output = 1
        curr = 1
        for i in range(1, len(nums)):
            curr = curr + 1 if nums[i] > nums[i-1] else 1
            output = max(output, curr)
        return output

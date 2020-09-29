class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        output = 0
        i = 0
        while i < len(nums):
            output += nums[i]
            i += 2
        return output

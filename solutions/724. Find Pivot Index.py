class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        for i in range(len(nums)):
            left = sum(nums[0:i])
            right = sum(nums[i+1:])
            if left == right:
                return i
        return -1

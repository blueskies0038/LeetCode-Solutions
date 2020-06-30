class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            for i in range(0, len(nums)):
                if nums[i] == target:
                    return i
        else:
            for i in range(0, len(nums)):
                if target <= nums[i]:
                    return i
                elif target > nums[len(nums) -1]:
                    return len(nums)
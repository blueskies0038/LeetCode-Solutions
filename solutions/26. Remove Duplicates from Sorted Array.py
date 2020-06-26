class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        i = 0
        if len(nums) == 1:
            return 1
        while i < len(nums) and len(nums) > 1:
            if nums[i] == nums[i-1]:
                del nums[i-1]
            else:
                i += 1
        return len(nums)
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        for j in range(len(nums)):
            if nums[j] == 0:
                nums[i], nums[j] = 0, nums[i]
                i += 1
        for j in range(len(nums)):
            if nums[j] == 1:
                nums[i], nums[j] = 1, nums[i]
                i += 1
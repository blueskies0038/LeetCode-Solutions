class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        i = 0
        nums.sort()
        while i < len(nums) - 1:
            if nums[i] == nums[i+1]:
                nums.pop(i)
                nums.pop(i)
            else:
                i += 1
                
        return nums

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        h = {}
        i = 0
        while i < len(nums):
            if nums[i] in h:
                if h[nums[i]] >= 2:
                    nums.remove(nums[i])
                else:
                    h[nums[i]] += 1
                    i += 1
            else:
                h[nums[i]] = 1
                i += 1
                
        return len(nums)

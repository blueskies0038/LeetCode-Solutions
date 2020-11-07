class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        output = 1
        for i, j in enumerate(nums):
            count = 0
            while j != -1:
                count += 1
                nums[i] = -1
                j = nums[j]
            output = max(output, count)
        return output

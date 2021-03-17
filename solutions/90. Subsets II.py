class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        output = [[]]
        nums.sort()
        
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i-1]:
                length = len(output)
            for j in range(len(output) - length, len(output)):
                output.append(output[j] + [nums[i]])
        
        return output

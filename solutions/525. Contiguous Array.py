class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = 0
        output = 0
        seen = {0: -1}
        
        for i in range(len(nums)):
            if nums[i] == 0:
                count -= 1
            if nums[i] == 1:
                count += 1
            
            if count in seen:
                output = max(output, i-seen[count])
            else:
                seen[count] = i
        
        return output

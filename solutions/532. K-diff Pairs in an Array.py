class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        output = []
        
        for i in range(len(nums) - 1):
            for j in range(i+1, len(nums)):
                if nums[j] - nums[i] > k:
                    break
                if nums[j] - nums[i] == k:
                    output.append(str(nums[j]) + str(nums[i]))
                    
        return len(set(output))

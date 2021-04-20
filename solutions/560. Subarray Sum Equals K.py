class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = {0: 1}
        currentSum = 0
        output = 0
        
        for i in range(len(nums)):
            currentSum += nums[i]
            if currentSum - k in count:
                output += count[currentSum-k]
            if currentSum in count:
                count[currentSum] += 1
            else:
                count[currentSum] = 1
                
        return output

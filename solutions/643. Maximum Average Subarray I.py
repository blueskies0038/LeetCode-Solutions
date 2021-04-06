class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxDelta = delta = 0
        
        for i in range(len(nums) - k):
            delta += nums[i+k] - nums[i]
            maxDelta = max(maxDelta, delta)
        
        return (sum(nums[:k]) + maxDelta) / k

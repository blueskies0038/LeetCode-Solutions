class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        rot = 0
        total = 0
        
        for i in range(n):
            rot += i * nums[i]
            total += nums[i]
        max_rot = rot
        
        for i in range(n - 1, 0, -1):
            rot = rot + total - n * nums[i]
            max_rot = max(max_rot, rot)
            
        return max_rot

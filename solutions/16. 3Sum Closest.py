class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        smallestDiff = math.inf
        
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                diff = target - nums[i] - nums[left] - nums[right]
                if diff == 0:
                    return target - diff
                if abs(diff) < abs(smallestDiff):
                    smallestDiff = diff
                if diff > 0:
                    left += 1
                else:
                    right -= 1
        
        return target - smallestDiff

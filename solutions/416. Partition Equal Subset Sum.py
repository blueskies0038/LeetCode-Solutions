class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        cache = {}
        def helper(index, target):
            if (index, target) in cache:
                return cache[(index, target)]
            if target < 0:
                return
            elif target == 0:
                return True
            for i in range(index, len(nums)):
                if helper(i+1, target-nums[i]):
                    return True
            cache[(index, target)] = False
            return False
        return False if sum(nums) % 2 else helper(0, sum(nums)/2)

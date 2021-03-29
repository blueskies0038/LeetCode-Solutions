class Solution:
    def minMoves(self, nums: List[int]) -> int:
        nums.sort()
        output = 0
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == nums[0]:
                break
            output += nums[i] - nums[0]
        return output

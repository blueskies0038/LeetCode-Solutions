class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        median = nums[int(len(nums)/2)]
        count = 0
        for i in nums:
            if i != median:
                count += abs(median-i)
        return count

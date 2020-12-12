class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = ones = 0
        for i in nums:
            if i == 1:
                count += 1
                ones = max(count, ones)
            else:
                count = 0
        return ones

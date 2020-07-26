class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        h ={}
        for num in nums:
            if num in h:
                return num
            h[num] = 1
        return None

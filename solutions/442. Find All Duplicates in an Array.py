class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        h = collections.defaultdict(int)
        for num in nums:
            h[num] += 1
        return [key for key, value in h.items() if value == 2]
​

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)/3
        h = Counter(nums)
        return [num for num in h.keys() if h[num] > n]

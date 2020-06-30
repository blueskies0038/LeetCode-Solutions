class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for index, val in enumerate(nums):
            if val == target:
                return index
        return -1
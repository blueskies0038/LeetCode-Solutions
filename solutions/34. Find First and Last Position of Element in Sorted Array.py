class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        position = []
        for index, val in enumerate(nums):
            if val == target:
                position.append(index)
        if len(position) == 0:
            return [-1, -1]
        else:
            return [min(position), max(position)]
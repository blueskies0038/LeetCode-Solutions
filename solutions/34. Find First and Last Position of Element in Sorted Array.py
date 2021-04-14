class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.searchLeft(nums, target)
        right = self.searchRight(nums, target)
        return [left, right]
        
    def searchLeft(self, nums, target):
        start, end = 0, len(nums) - 1
        index = -1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                index = mid
                end = mid - 1
        return index
    
    def searchRight(self, nums, target):
        start, end = 0, len(nums) - 1
        index = -1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                index = mid
                start = mid + 1
        return index

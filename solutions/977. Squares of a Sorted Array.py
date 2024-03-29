class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        output = [0 for i in range(len(nums))]
        left, right = 0, len(nums) - 1
        for index in range(len(nums)-1, -1, -1):
            if abs(nums[left]) > abs(nums[right]):
                output[index] = nums[left] ** 2
                left += 1
            else:
                output[index] = nums[right] ** 2
                right -= 1
        return output

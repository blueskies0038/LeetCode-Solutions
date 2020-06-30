class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        length = len(nums)
        while i < length:
            if nums[i] == val:
                nums.pop(i)
                length = length - 1
            else:
                i += 1
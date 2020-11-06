class Solution:
    def solution(self, nums, output, curr, index):
        if index >= len(nums):
            return output
        output.append(curr[:])
        for i in range(index, len(nums)):
            if nums[i] not in curr:
                curr.append(nums[i])
                self.solution(nums, output, curr, i)
                curr.pop()
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        curr = []
        self.solution(nums, output, curr, 0)
        return output

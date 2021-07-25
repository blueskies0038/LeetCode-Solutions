class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()
        self.dfs(nums, [], output)
        return output
    
    def dfs(self, nums, path, output):
        if not nums:
            output.append(path)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                    continue
            self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], output)

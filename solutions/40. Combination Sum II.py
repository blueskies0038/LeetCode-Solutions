class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        self.dfs(sorted(candidates), target, 0, [], output)
        return output
        
    def dfs(self, nums, target, index, path, output):
        if target <= 0:
            if target == 0:
                output.append(path)
            return 
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i-1]:
                continue
            self.dfs(nums, target - nums[i], i + 1, path + [nums[i]], output)

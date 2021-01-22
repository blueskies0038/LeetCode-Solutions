class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        sol = []
        
        self.dfs(candidates, target, [], sol)
        return sol
    
    def dfs(self, nums, target, path, sol):
        if target < 0:
            return 
            
        if target == 0:
            sol.append(path)
            return 
            
        for i in range(len(nums)):
            self.dfs(nums[i:], target - nums[i], path + [nums[i]], sol)
​

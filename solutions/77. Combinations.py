class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        output = []
        self.dfs(list(range(1, n+1)), k, [], output)
        return output
    
    def dfs(self, nums, k, path, output):
        if len(path) == k:
            output.append(path)
            return
        
        for i in range(len(nums)):
            self.dfs(nums[i+1:], k, path+[nums[i]], output)

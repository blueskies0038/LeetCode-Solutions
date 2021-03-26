class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        output = []
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.dfs(nums, k, n, [], output)
        return output
        
    def dfs(self, nums, k, target, path, output):
        if k < 0 or target < 0:
            return
        if k == 0 and target == 0:
            output.append(path)
        for i in range(len(nums)):
            self.dfs(nums[i+1:], k - 1, target - nums[i], path + [nums[i]], output)

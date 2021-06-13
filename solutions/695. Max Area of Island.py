class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        output = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    output = max(self.dfs(i, j, grid), output)
                    
        return output
        
    def dfs(self, row, col, grid):
        if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[row]) or grid[row][col] == 0:
            return 0
​
        grid[row][col] = 0
​
        up = self.dfs(row, col+1, grid)
        down = self.dfs(row, col-1, grid)
        left = self.dfs(row-1, col, grid)
        right = self.dfs(row+1, col, grid)
​
        return up + down + left + right + 1

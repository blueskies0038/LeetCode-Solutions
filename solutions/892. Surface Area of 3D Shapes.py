class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        n, output = len(grid), 0
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    output += 2 + grid[i][j] * 4
                if i:
                    output -= min(grid[i][j], grid[i - 1][j]) * 2
                if j:
                    output -= min(grid[i][j], grid[i][j - 1]) * 2
        return output

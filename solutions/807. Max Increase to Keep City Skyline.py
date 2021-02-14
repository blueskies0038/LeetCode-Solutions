class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        row, col = [max(r) for r in grid], [max(c) for c in zip(*grid)]
        output = 0
        for i in range(m):
            for j in range(n):
                output += min(row[i], col[j]) - grid[i][j]
        return output

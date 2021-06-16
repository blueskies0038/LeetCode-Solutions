class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        queue, m, n = [], len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] != 0:
                    matrix[i][j] = float("inf")
                else:
                    queue.append((i, j))
                    
        for i, j in queue:
            for r, c in ((i, 1+j), (i, j-1), (i+1, j), (i-1, j)):
                z = matrix[i][j] + 1
                if 0 <= r < m and 0 <= c < n and matrix[r][c] > z:
                    matrix[r][c] = z
                    queue.append((r, c))
                    
        return matrix

class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        y, x = next((i, j) for j in range(8) for i in range(8) if board[i][j] == 'R')
        row = ''.join(board[y][j] for j in range(8) if board[y][j] != '.')
        col = ''.join(board[i][x] for i in range(8) if board[i][x] != '.')
        return sum('Rp' in s for s in (row, col)) + sum('pR' in s for s in (row, col))

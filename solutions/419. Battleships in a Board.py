class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        if len(board) == 0:
            return 0
        m = len(board)
        n = len(board[0])
        ships = 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X' and (i == 0 or board[i-1][j] == '.') and (j == 0 or board[i][j-1] == '.'):
                    ships += 1
        return ships

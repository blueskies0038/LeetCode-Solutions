class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        found = False
        
        def dfs(board, row, col, count, word):
            if count == len(word):
                nonlocal found
                found = True
                return
            
            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col] != word[count] or found:
                return
            
            temp = board[row][col]
            board[row][col] = " "
            dfs(board, row - 1, col, count + 1, word)
            dfs(board, row + 1, col, count + 1, word)
            dfs(board, row, col - 1, count + 1, word)
            dfs(board, row, col + 1, count + 1, word)
            
            board[row][col] = temp
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    dfs(board, row, col, 0, word)
        
        return found
​

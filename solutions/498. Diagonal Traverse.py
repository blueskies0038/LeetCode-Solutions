class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0:
            return []
        m = len(matrix[0]) - 1
        n = len(matrix) - 1
        down = True
        row = col =  0
        output = []
        while not self.out(row, col, n, m):
            output.append(matrix[row][col])
            if down:
                if col == m or row == 0:
                    down = False
                    if col == m:
                        row += 1
                    else:
                        col += 1
                else:
                    row -= 1
                    col += 1
            
            else:
                if col == 0 or row == n:
                    down = True
                    if row == n:
                        col += 1
                    else:
                        row += 1
                else:
                    row += 1
                    col -= 1
        return output
            
    def out(self, row, col, n, m):
        return row < 0 or row > n or col < 0 or col > m

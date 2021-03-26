class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        output = 0
        for i in range(len(mat)):
            output += mat[i][i]
            output += mat[i][len(mat)-i-1]
        
        if len(mat) % 2 == 1:
            output -= mat[len(mat)//2][len(mat)//2]
        
        return output

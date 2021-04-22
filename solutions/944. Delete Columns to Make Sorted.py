class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        output = 0
        
        for col in range(len(A[0])):
            for row in range(len(A) - 1):
                if A[row][col] > A[row+1][col]:
                    output += 1
                    break 
    
        return output

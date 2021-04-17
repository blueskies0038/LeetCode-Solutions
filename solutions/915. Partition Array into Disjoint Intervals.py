class Solution:
    def partitionDisjoint(self, A: List[int]) -> int:
        current = candidate = A[0]
        output = 1
        
        for i in range(1, len(A)):
            if A[i] < current:
                output = i + 1
                current = candidate
            elif A[i] > candidate:
                candidate = A[i]
        
        return output
                

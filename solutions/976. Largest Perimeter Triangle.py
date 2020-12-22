class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        if len(A) == 3:
            if A[0] + A[1] > A[2] and A[1] + A[2] > A[0] and A[0] + A[2] > A[1]:
                return sum(A)
            else:
                return 0
            
        A = sorted(A, reverse=True)
                
        for i in range(0, len(A) - 2):
            if A[i] + A[i+1] > A[i+2] and A[i+1] + A[i+2] > A[i] and A[i] + A[i+2] > A[i+1]:
                return A[i] + A[i+1] + A[i+2]
        
        return 0

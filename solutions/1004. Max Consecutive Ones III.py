class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        start, max_length, max_ones = 0, 0, 0
        
        for end in range(len(A)):
            if A[end] == 1:
                max_ones += 1
            
            if end - start + 1 - max_ones > K:
                if A[start] == 1:
                    max_ones -= 1
                start +=1 
            
            max_length = max(max_length, end - start + 1)
            
        return max_length

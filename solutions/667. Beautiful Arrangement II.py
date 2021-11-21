class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        if k >= n : 
            return []
        output = [i+1 for i in range(n)]
        i = 1
        
        while i < k:
            output = output[:i] + output[i:][::-1]
            i += 1
            
        return output

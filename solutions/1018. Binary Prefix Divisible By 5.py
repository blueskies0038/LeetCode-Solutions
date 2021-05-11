class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        answer = [None] * len(A)
        S = 0
        
        for index, i in enumerate(A):
            S <<= 1
            S += i
            S %= 5
            answer[index] = S == 0
        
        return answer

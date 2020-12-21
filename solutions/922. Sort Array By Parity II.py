class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        i = 0
        j = 1
        a = len(A)
        while i < a and j < a:
            while i < a and A[i]%2 == 0:
                i += 2
            while j < a and A[j]%2 == 1:
                j += 2
            if i < a and j < a:
                A[i], A[j] = A[j], A[i]
        return A

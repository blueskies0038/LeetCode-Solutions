class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        new_A = sorted(A)
        return new_A == A or new_A == A[::-1]

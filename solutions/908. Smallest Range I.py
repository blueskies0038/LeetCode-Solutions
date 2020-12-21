class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        mx = max(A)
        mn = min(A)
        return max(0, mx - mn - 2*K)

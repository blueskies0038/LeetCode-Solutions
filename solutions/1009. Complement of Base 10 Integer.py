class Solution:
    def bitwiseComplement(self, N: int) -> int:
        P = 2
        while P <= N:
            P *= 2
        return P - 1 - N

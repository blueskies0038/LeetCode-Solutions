class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        L = int(area**0.5)
        while area % L > 0:
            L += 1
        W = int(area/L)
        return [max(L, W), min(L, W)]

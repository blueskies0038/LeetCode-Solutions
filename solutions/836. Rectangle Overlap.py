class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        r1 = max(rec1[0], rec2[0]) < min(rec1[2], rec2[2])
        r2 = max(rec1[1], rec2[1]) < min(rec1[3], rec2[3])
        return r1 and r2

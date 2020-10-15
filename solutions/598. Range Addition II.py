class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        row = m
        col = n
        for op in ops:
            row = min(row, op[0])
            col = min(col, op[1])
        return row*col

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        work = sorted(zip(difficulty, profit))
        mp = mx = i = 0
        for w in sorted(worker):
            while i < len(work) and work[i][0] <= w:
                mx = max(mx, work[i][1])
                i += 1
            mp += mx
        return mp

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) <= 1:
            return 0
        intervals.sort()
        end = intervals[0][0] - 1
        no_overlap = 0
        for interval in intervals:
            if interval[0] < end:
                end = min(end, interval[1])
            else:
                no_overlap += 1
                end = interval[1]
        return len(intervals) - no_overlap

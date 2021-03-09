class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return []
        
        intervals = sorted(intervals, key = lambda x: x[0])
        output = [intervals[0]]
        
        for i in intervals[1:]:
            if i[0] <= output[-1][1]:
                output[-1][1] = max(i[1], output[-1][1])
            else:
                output.append(i)
        
        return output

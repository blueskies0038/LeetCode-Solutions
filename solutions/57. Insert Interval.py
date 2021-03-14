class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        output = []
        
        for i in sorted(intervals, key = lambda x: x[0]):
            if output and output[-1][1] >= i[0]:
                output[-1][1] = max(output[-1][1], i[1])
            else:
                output.append(i)
        
        return output

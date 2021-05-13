class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        currentMax = output = 0
        
        for i, v in enumerate(values):
            output = max(output, v - i + currentMax)
            currentMax = max(currentMax, v + i)
        
        return output

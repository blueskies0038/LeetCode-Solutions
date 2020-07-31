class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        output = 0
        stack = []
        heights.insert(0,0)
        heights.append(0)
​
        for index, height in enumerate(heights):   
            while stack and heights[stack[-1]] > height:
                j = stack.pop()
                output = max(output, (index - stack[-1] - 1) * heights[j])
            stack.append(index)
            
        return output

class Solution:
    def maxArea(self, height: List[int]) -> int:
        volume = 0
        head = 0
        tail = len(height) - 1
        for i in height:
            width = abs(tail - head)
            if height[head] < height[tail]:
                water = width * height[head]
                head += 1
            else:
                water = width * height[tail]
                tail -= 1
            if water > volume:
                volume = water
        return volume
            
                    
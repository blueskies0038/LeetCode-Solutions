class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        h1 = 0
        h2 = 0
        for i in range(len(height)):
            h1 = max(h1, height[i])
            h2 = max(h2, height[-i-1])
            water = water + h1 + h2 - height[i]
        return water - len(height)*h1
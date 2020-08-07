class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        x = y = ans = 0
        z = 1
        for num in nums:
            if num == 1:
                y += 1
                ans = max(ans, x + y)
            else:
                x, y = y, 0
                z = 0
        return ans - z

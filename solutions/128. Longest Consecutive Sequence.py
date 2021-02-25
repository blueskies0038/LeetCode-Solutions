class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        output = 0
        
        h = {}
        for num in nums:
            if num not in h:
                h[num] = True
        
        for num in nums:
            if num - 1 not in h:
                curr = num
                streak = 1
                
                while curr + 1 in h:
                    curr += 1
                    streak += 1
                
                output = max(streak, output)
                
        return output

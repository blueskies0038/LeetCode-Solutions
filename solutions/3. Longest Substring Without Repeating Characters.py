class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, max_length = 0, 0
        h = {}
        
        for end in range(len(s)):
            char = s[end]
            
            if char in h:
                start = max(start, h[char] + 1)
        
            h[char] = end
            max_length = max(max_length, end - start + 1)
        
        return max_length

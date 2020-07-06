class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        max_length = 0
        window_start = 0
        for i in range(len(s)):
            end = s[i]
            if end in char_map and char_map[end] >= window_start:
                window_start = char_map[end] + 1
            char_map[end] = i
            max_length = max(max_length, i - window_start + 1)
        return max_length
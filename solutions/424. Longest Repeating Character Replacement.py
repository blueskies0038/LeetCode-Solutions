class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start, max_length, max_repeat_count = 0, 0, 0
        frequency = collections.defaultdict(int)
        
        for end in range(len(s)):
            right_char = s[end]
            frequency[right_char] += 1
            max_repeat_count = max(max_repeat_count, frequency[right_char])
            
            if end - start + 1 - max_repeat_count > k:
                left_char = s[start]
                frequency[left_char] -= 1
                start += 1
        
            max_length = max(max_length, end - start + 1)
        
        return max_length

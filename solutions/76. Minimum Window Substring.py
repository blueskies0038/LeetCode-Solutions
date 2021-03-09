class Solution:
    def minWindow(self, s: str, t: str) -> str:
        start, matches, sub_start = 0, 0, 0
        freq = {}
        min_length = len(s) + 1
        
        for ch in t:
            if ch not in freq:
                freq[ch] = 0
            freq[ch] += 1
            
        for end in range(len(s)):
            right_char = s[end]
            if right_char in freq:
                freq[right_char] -= 1
                if freq[right_char] >= 0:
                    matches += 1
        
            while matches == len(t):
                if min_length > end - start + 1:
                    min_length = end - start + 1
                    sub_start = start
                left_char = s[start]
                start += 1
                if left_char in freq:
                    if freq[left_char] == 0:
                        matches -= 1
                    freq[left_char] += 1
        
        if min_length > len(s):
            return ""
        return s[sub_start: sub_start+min_length]

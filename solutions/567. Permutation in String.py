class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        start, matches = 0, 0
        letters = {}
        
        for i in s1:
            if i not in letters:
                letters[i] = 0
            letters[i] += 1
        
        for end in range(len(s2)):
            right_char = s2[end]
            
            if right_char in letters:
                letters[right_char] -= 1
                if letters[right_char] == 0:
                    matches += 1
            
            if matches == len(letters):
                return True
            
            if end >= len(s1) - 1:
                left_char = s2[start]
                start += 1
                if left_char in letters:
                    if letters[left_char] == 0:
                        matches -= 1
                    letters[left_char] += 1
        
        return False

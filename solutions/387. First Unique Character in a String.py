class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for c in s:
            if c not in d:
                d[c] = 1
            else:
                d[c] += 1
        
        index = -1
        for i in range(len(s)):
            if d[s[i]] == 1:
                index = i
                break
        
        return index

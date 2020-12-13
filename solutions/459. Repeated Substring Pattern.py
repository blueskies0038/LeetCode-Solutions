class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if not s:
            return False
        sec = ""
        n = len(s)
        i = 0
        while i < n//2:
            sec = sec + s[i]
            i = i + 1
            t = ceil(n/i)
​
            if sec * t == s:
                return True
        return False

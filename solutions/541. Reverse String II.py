class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        if len(s) <= k:
            return s[::-1]
        if len(s) <= 2*k:
            return s[:k][::-1] + s[k:]
        
        i = 0
        j = k
        ans = ''
        while i < len(s):
            ans += s[i:j][::-1] + s[j:j+k]
            i = j + k
            j = i + k
        return ans

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        h = {}
        for i in s:
            if i in h:
                h[i] += 1
            else:
                h[i] = 1
        for j in t:
            if j not in h:
                return False
            h[j] -= 1
            if h[j] < 0:
                return False
        return True

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack and len(needle) > 0:
            for i in range(0, len(haystack)):
                if haystack[i: i+len(needle)] == needle:
                    return i
        elif len(needle) == 0:
            return 0
        else:
            return -1
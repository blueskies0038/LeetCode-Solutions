class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ''
        output = ''
        for i in range(len(s)):
            current = self.expand(s, i-1, i+1)
            between = self.expand(s, i, i+1)
            output = max(output, current, between, key=len)
        return output
    def expand(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        sen = s.strip()
        words = sen.split(" ")
        return len(words[-1])
class Solution:
    def reverseWords(self, s: str) -> str:
        splited = s.split()
        output = " ".join(splited[::-1])
        return output
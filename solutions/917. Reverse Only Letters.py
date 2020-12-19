class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        left = 0
        right = len(S) - 1
        while left < right:
            if S[left].isalpha() and S[right].isalpha():
                S = S[:left] + S[right] + S[left+1:right] + S[left] + S[right+1:]
                left += 1
                right -= 1
            elif S[left].isalpha():
                right -= 1
            else: left += 1
        return S

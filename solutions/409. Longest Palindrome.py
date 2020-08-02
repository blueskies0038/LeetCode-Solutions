class Solution:
    def longestPalindrome(self, s: str) -> int:
        output = 0
        letters = Counter(s)
        for i in letters:
            if letters[i] > 1:
                output += (letters[i]) - (letters[i])%2
        if len(s) != output:
            output += 1
        return output
        

class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        add = 0
        for i in range(len(shifts)-1, -1, -1):
            add += shifts[i] % 26
            shifts[i] = add
        
        output = ''
        for i in range(len(S)):
            shifted = (ord(S[i]) - 97 + shifts[i]) % 26
            output += chr(shifted + 97)
        return output

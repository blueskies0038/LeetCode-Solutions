class Solution:
    def addBinary(self, a: str, b: str) -> str:
        total = str(bin(int(a, 2) + int(b, 2)))[2:]
        return total
class Solution:
    def binaryGap(self, n: int) -> int:
        binary = bin(n)
        left, right = 0, 0
        output = 0
        
        for i in range(2, len(binary)):
            if binary[i] == "1":
                if left == 0:
                    left = i
                else:
                    right = i
                    output = max(right - left, output)
                    left = right
        return output

class Solution:
    def baseNeg2(self, n: int) -> str:
        output = []
        while n != 0:
            r = n % (-2)
            if r == -1:
                r = 1
            n = (n - r) // (-2)
​
            output.append(str(r))
            
        return ''.join(output[::-1]) or "0"

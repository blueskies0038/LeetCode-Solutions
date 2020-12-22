class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        if X > Y:
            return X - Y
        if X == Y:
            return 0
        output = 0
        while Y > X:
            output += 1
            if Y % 2:
                Y += 1
            else:
                Y /= 2
        return int(output + X - Y)

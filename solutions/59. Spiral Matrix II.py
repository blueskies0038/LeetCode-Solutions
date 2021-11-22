class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        output, low = [], n*n+1
        while low > 1:
            low, high = low - len(output), low
            output = [range(low, high)] + list(zip(*output[::-1]))
        return output

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        output = [""]*numRows
        if numRows == 1 or numRows >= len(s):
            return s
        index = 0
        step = 1
        for letter in s:
            output[index] += letter
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step
        return ''.join(output)
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        integer = ""
        for digit in digits:
            integer = integer + str(digit)
        output = [digit for digit in str(int(integer) + 1)]
        return output
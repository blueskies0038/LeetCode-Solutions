class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n < 5:
            return 0
        multiples_Array =[]
        multiple = 5
        while multiple <= n:
            multiples_Array.append(multiple)
            multiple *= 5
        result = 0
        for i in multiples_Array:
            result += n//i
        return result

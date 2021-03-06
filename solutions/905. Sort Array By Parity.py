class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        even = [num for num in A if num % 2 == 0]
        odd = [num for num in A if num % 2 == 1]
        return even + odd

class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        return [[1 - i for i in r[::-1]] for r in A]

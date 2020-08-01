class Solution:
    def arrangeCoins(self, n: int) -> int:
        def findRows(rows, coins, i):
            if coins - i < 0:
                return rows
            return findRows(rows+1, coins-i, i + 1)
        return findRows(0, n, 1)

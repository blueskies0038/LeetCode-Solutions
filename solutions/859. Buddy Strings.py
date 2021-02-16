class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        count_A, count_B = Counter(A), Counter(B)
        if count_A != count_B:
            return False
        diff = sum([i != j for i, j in zip(A, B)])
        if diff != 0 and diff != 2:
            return False
        if diff == 0 and len(count_A) == len(A):
            return False
        return True

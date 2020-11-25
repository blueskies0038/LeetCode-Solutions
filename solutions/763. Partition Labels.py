class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        d = {char: idx for idx, char in enumerate(S)}
        output = []
        left = right = 0
        for i, c in enumerate(S):
            right = max(right, d[c])
            if i == right:
                output.append(right - left + 1)
                left = i + 1
        return output

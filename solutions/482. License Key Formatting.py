class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        S = "".join(S[::-1].upper().split("-"))
        output = []
        for i in range(0, len(S), K):
            output.append(S[i:i+K])
        return "-".join(output)[::-1]

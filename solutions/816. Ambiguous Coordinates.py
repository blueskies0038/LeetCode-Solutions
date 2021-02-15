class Solution:
    def ambiguousCoordinates(self, S: str) -> List[str]:
        S = S[1:-1]
        output = []
        for i in range(1, len(S)): 
            output.extend([f"({x}, {y})" for x in self.findDecimal(S[:i]) for y in self.findDecimal(S[i:])])
        return output
    
    def findDecimal(self, S):
        if len(S) == 1:
            return [S]
        if S.startswith("0") and S.endswith("0"):
            return []
        if S.startswith("0"):
            return [S[:1] + "." + S[1:]]
        if S.endswith("0"):
            return [S]
        return [S] + [S[:i] + "." + S[i:] for i in range(1, len(S))]
​

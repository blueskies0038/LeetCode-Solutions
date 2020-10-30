class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        tokens.sort()
        i, j = 0, len(tokens)-1
        output = score = 0
​
        while i <= j and (P >= tokens[i] or score > 0):
            while i <= j and P >= tokens[i]:
                P -= tokens[i]
                score += 1
                i += 1
            output = max(output, score)
​
            if i <= j and score:
                P += tokens[j]
                score -= 1
                j -= 1
​
        return output

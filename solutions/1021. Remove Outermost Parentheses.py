class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        output = []
        total = 0
        i = 0
        for j in range(len(S)):
            if S[j] == "(":
                total += 1
            elif S[j] == ")":
                total -= 1
            if total == 0:
                output.append(S[i+1:j])
                i = j+1
        return "".join(output)

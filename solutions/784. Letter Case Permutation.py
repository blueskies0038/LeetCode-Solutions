class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        output = []
        output.append(S)
        
        for i in range(len(S)):
            if S[i].isalpha():
                for j in range(len(output)):
                    perm = list(output[j])
                    perm[i] = perm[i].swapcase()
                    output.append("".join(perm))
        
        return output

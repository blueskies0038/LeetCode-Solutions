class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        if len(strs) > 0:
            for i in range(len(min(strs))):
                new = prefix + strs[0][i]
                for j in range(len(strs)):
                    if strs[0][i] != strs[j][i]:
                        return prefix
                prefix = new
        return prefix
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        self.dfs(n, n, "", output)
        return output
        
    def dfs(self, leftCount, rightCount, path, output):
        if rightCount < leftCount or rightCount < 0 or leftCount < 0:
            return
        if leftCount == 0 and rightCount == 0:
            output.append(path)
            return
        self.dfs(leftCount - 1, rightCount, path + "(", output)
        self.dfs(leftCount, rightCount - 1, path + ")", output)

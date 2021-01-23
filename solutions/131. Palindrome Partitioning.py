class Solution:
    def partition(self, s: str) -> List[List[str]]:
        output = []
        self.dfs(s, [], output)
        return output
​
    def dfs(self, s, path, output):
        if not s:
            output.append(path)
            return
        for i in range(1, len(s) + 1):
            if self.isPal(s[:i]):
                self.dfs(s[i:], path + [s[:i]], output)
​
    def isPal(self, s):
        return s == s[::-1]

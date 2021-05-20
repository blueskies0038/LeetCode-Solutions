class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        self.output = set()
        self.dfs("", tiles)
        return len(self.output)
        
    def dfs(self, path, tiles):
        if path not in self.output:
            if path:
                self.output.add(path)
            for i in range(len(tiles)):
                self.dfs(path + tiles[i], tiles[:i] + tiles[i+1:])

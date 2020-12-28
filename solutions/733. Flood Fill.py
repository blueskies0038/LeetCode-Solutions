class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])
        change = image[sr][sc]
        
        def dfs(r, c, rows, cols, newColor, image, change):            
            if r < 0 or c < 0 or r > rows-1 or c > cols-1 or image[r][c] == newColor or image[r][c] != change:
                return
            
            image[r][c] = newColor
            
            dfs(r+1, c, rows, cols, newColor, image, change)
            dfs(r-1, c, rows, cols, newColor, image, change)
            dfs(r, c+1, rows, cols, newColor, image, change)
            dfs(r, c-1, rows, cols, newColor, image, change)
        
        dfs(sr, sc, rows, cols, newColor, image, change)
        
        return image

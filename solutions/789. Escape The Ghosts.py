class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        x,y=target
        dist=abs(x)+abs(y)
        for i,j in ghosts:
            if dist>=abs(x-i)+abs(y-j):
                return False
        return True
